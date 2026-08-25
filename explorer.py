cat << 'EOF' > explorador.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import time
import shutil
import subprocess
from pathlib import Path

R  = "\033[1;31m"
G  = "\033[1;32m"
Y  = "\033[1;33m"
B  = "\033[1;34m"
M  = "\033[1;35m"
C  = "\033[1;36m"
W  = "\033[1;37m"
D  = "\033[0m"

def clear():
    os.system("clear" if os.name != "nt" else "cls")

def type_effect(text, delay=0.028):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def spinner(msg, sec=1.2):
    frames = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
    end = time.time() + sec
    i = 0
    while time.time() < end:
        sys.stdout.write(f"\r{C}  {frames[i % len(frames)]} {msg}{D}   ")
        sys.stdout.flush()
        time.sleep(0.09)
        i += 1
    sys.stdout.write("\r" + " " * 55 + "\r")
    sys.stdout.flush()

def human_size(n):
    for u in ["B", "KB", "MB", "GB", "TB"]:
        if n < 1024:
            return f"{n:.1f} {u}"
        n /= 1024
    return f"{n:.1f} PB"

def get_start_path():
    for p in ["/storage/emulated/0", "/sdcard", "/storage/emulated",
              str(Path.home() / "storage" / "shared"),
              os.path.expanduser("\~"), "/"]:
        if os.path.isdir(p) and os.access(p, os.R_OK):
            return p
    return os.getcwd()

def ensure_permissions():
    """Só mostra tela se NÃO tiver permissão. Se já tiver, não faz nada."""
    storage_dir = Path.home() / "storage"
    shared = storage_dir / "shared"

    # Já tem permissão? → sai silencioso
    if storage_dir.exists() and shared.exists() and os.access(str(shared), os.R_OK | os.W_OK):
        return True

    # Não tem permissão → pede
    clear()
    print(f"{Y}")
    print("  ╭────────────────────────────────────╮")
    print("  │                                    │")
    print("  │     ⚠  PERMISSÃO NECESSÁRIA        │")
    print("  │                                    │")
    print("  ╰────────────────────────────────────╯")
    print(f"{D}")
    print(f"\n{W}  O explorador precisa de acesso aos arquivos.{D}")
    print(f"{Y}  Vou abrir a tela de permissões agora.{D}")
    print(f"{Y}  Toque em Permitir / Allow.{D}\n")
    input(f"{C}  ENTER para continuar…{D}")

    try:
        os.system("termux-setup-storage")
    except:
        pass

    time.sleep(1.5)

    if (Path.home() / "storage").exists():
        clear()
        print(f"\n{G}  ✅  Permissão concedida!{D}")
        time.sleep(1.2)
        return True
    else:
        clear()
        print(f"\n{Y}  ⚠  Permissão ainda não detectada.{D}")
        print(f"{W}  Você pode conceder depois em:")
        print(f"{W}  Configurações → Apps → Termux → Permissões{D}")
        input(f"\n{C}  ENTER para continuar mesmo assim…{D}")
        return False

def listar(path):
    try:
        itens = os.listdir(path)
    except PermissionError:
        return [], [], "Sem permissão de leitura"
    except Exception as e:
        return [], [], str(e)

    dirs, files = [], []
    for nome in sorted(itens, key=str.lower):
        full = os.path.join(path, nome)
        try:
            if os.path.isdir(full):
                dirs.append(nome)
            else:
                files.append(nome)
        except:
            continue
    return dirs, files, None

def desenhar_borda(caminho, clipboard=None):
    print(f"{C}  ╭────────────────────────────────────╮")
    print(f"{C}  │  📁  EXPLORADOR  •  Healing_Boy85  │")
    print(f"{C}  ├────────────────────────────────────┤")

    if len(caminho) > 32:
        caminho_show = "…" + caminho[-31:]
    else:
        caminho_show = caminho
    print(f"{C}  │  📍 {caminho_show:<32} │")

    if clipboard:
        nome = os.path.basename(clipboard)
        if len(nome) > 26:
            nome = nome[:23] + "…"
        print(f"{C}  │  ✂️  Mover: {nome:<26} │")

    print(f"{C}  ╰────────────────────────────────────╯{D}")

def criar_pasta(atual):
    clear()
    print(f"{C}  ╭────────────────────────────────────╮")
    print(f"{C}  │  📁  CRIAR NOVA PASTA              │")
    print(f"{C}  ╰────────────────────────────────────╯{D}\n")
    nome = input(f"{C}  Nome da pasta → {W}").strip()
    if not nome:
        print(f"\n{Y}  Nome vazio. Cancelado.{D}")
        time.sleep(1.0)
        return
    nome = nome.replace("/", "_").replace("\\", "_").replace("..", "_")
    destino = os.path.join(atual, nome)
    try:
        os.mkdir(destino)
        spinner(f"Criando “{nome}”…", 0.8)
        print(f"\n{G}  ✅  Pasta criada!{D}")
        time.sleep(1.0)
    except FileExistsError:
        print(f"\n{R}  Já existe uma pasta com esse nome.{D}")
        time.sleep(1.1)
    except Exception as e:
        print(f"\n{R}  Erro: {e}{D}")
        time.sleep(1.1)

def renomear_arquivo(atual, files):
    clear()
    print(f"{C}  ╭────────────────────────────────────╮")
    print(f"{C}  │  ✏️  RENOMEAR ARQUIVO              │")
    print(f"{C}  ╰────────────────────────────────────╯{D}\n")

    if not files:
        print(f"{Y}  Nenhum arquivo nesta pasta.{D}")
        time.sleep(1.0)
        return

    print(f"{W}  Escolha o arquivo:{D}\n")
    for i, f in enumerate(files, 1):
        print(f"  {Y}{i:2d}.{D}  {W}{f}{D}")

    try:
        escolha = input(f"\n{C}  Número → {W}").strip()
        idx = int(escolha) - 1
        if not (0 <= idx < len(files)):
            print(f"\n{R}  Número inválido.{D}")
            time.sleep(1.0)
            return
    except:
        print(f"\n{R}  Entrada inválida.{D}")
        time.sleep(1.0)
        return

    nome_original = files[idx]
    base, extensao = os.path.splitext(nome_original)

    clear()
    print(f"{C}  ╭────────────────────────────────────╮")
    print(f"{C}  │  ✏️  RENOMEAR ARQUIVO              │")
    print(f"{C}  ╰────────────────────────────────────╯{D}\n")
    print(f"{W}  Atual     : {Y}{nome_original}{D}")
    print(f"{W}  Extensão  : {G}{extensao or '(nenhuma)'}{D}")
    print(f"{Y}  (a extensão NÃO será mudada){D}\n")

    novo_base = input(f"{C}  Novo nome (sem extensão) → {W}").strip()
    if not novo_base:
        print(f"\n{Y}  Cancelado.{D}")
        time.sleep(0.9)
        return

    novo_base = novo_base.replace("/", "_").replace("\\", "_").replace("..", "_")
    novo_nome = novo_base + extensao
    origem = os.path.join(atual, nome_original)
    destino = os.path.join(atual, novo_nome)

    if os.path.exists(destino):
        print(f"\n{R}  Já existe “{novo_nome}”.{D}")
        time.sleep(1.1)
        return

    try:
        spinner("Renomeando…", 0.8)
        os.rename(origem, destino)
        print(f"\n{G}  ✅  Renomeado!{D}")
        print(f"{W}  {nome_original} → {novo_nome}{D}")
        time.sleep(1.3)
    except Exception as e:
        print(f"\n{R}  Erro: {e}{D}")
        time.sleep(1.1)

def mover_aqui(atual, clipboard):
    if not clipboard or not os.path.exists(clipboard):
        print(f"\n{Y}  Nada para colar.{D}")
        time.sleep(0.9)
        return None

    nome = os.path.basename(clipboard)
    destino = os.path.join(atual, nome)

    if os.path.exists(destino):
        conf = input(f"{Y}  Já existe “{nome}”. Sobrescrever? (s/n) → {W}").strip().lower()
        if conf not in ("s", "sim", "y"):
            print(f"{Y}  Cancelado.{D}")
            time.sleep(0.9)
            return clipboard

    try:
        spinner(f"Movendo “{nome}”…", 1.0)
        shutil.move(clipboard, destino)
        print(f"\n{G}  ✅  Movido com sucesso!{D}")
        time.sleep(1.0)
        return None
    except Exception as e:
        print(f"\n{R}  Erro: {e}{D}")
        time.sleep(1.1)
        return clipboard

def abrir_arquivo(caminho):
    nome = os.path.basename(caminho)
    ext  = os.path.splitext(nome)[1].lower()
    clear()
    print(f"{C}  ╭────────────────────────────────────╮")
    print(f"{C}  │  📄  ARQUIVO SELECIONADO           │")
    print(f"{C}  ╰────────────────────────────────────╯{D}\n")
    print(f"{W}  Nome    : {Y}{nome}{D}")
    try:
        print(f"{W}  Tamanho : {Y}{human_size(os.path.getsize(caminho))}{D}")
    except:
        pass
    print(f"{W}  Tipo    : {Y}{ext or 'sem extensão'}{D}\n")

    if ext in (".apk", ".hb"):
        tipo = "APK" if ext == ".apk" else "HB"
        print(f"{G}  Arquivo {tipo} detectado.{D}")
        conf = input(f"\n{C}  Deseja instalar? (s/n) → {W}").strip().lower()
        if conf in ("s", "sim", "y"):
            spinner("Abrindo instalador de pacote…")
            try:
                subprocess.run([
                    "termux-open",
                    "--content-type", "application/vnd.android.package-archive",
                    caminho
                ], check=False)
            except:
                try:
                    subprocess.run([
                        "am", "start",
                        "-a", "android.intent.action.VIEW",
                        "-t", "application/vnd.android.package-archive",
                        "-d", "file://" + caminho
                    ], check=False)
                except Exception as e:
                    print(f"\n{R}  Erro: {e}{D}")

            print(f"\n{G}  Instalador de pacote aberto!{D}")
            print(f"\n{Y}  ⚠  Se o botão INSTALAR não funcionar:{D}")
            print(f"{W}  1. Configurações → Apps → Acesso especial")
            print(f"{W}  2. Instalar apps desconhecidos")
            print(f"{W}  3. Ative a permissão para o Termux{D}")
            input(f"\n{C}  ENTER para voltar{D}")
        return

    if ext in (".mp4", ".mkv", ".webm", ".avi", ".mov", ".3gp"):
        print(f"{G}  Vídeo detectado.{D}")
        print(f"\n{W}  1. Abrir   2. Cancelar{D}")
        if input(f"{C}  → {W}").strip() == "1":
            spinner("Abrindo vídeo…")
            tentar_abrir(caminho)
        return

    if ext in (".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".heic"):
        print(f"{G}  Imagem detectada.{D}")
        if input(f"{C}  Abrir na galeria? (s/n) → {W}").strip().lower() in ("s", "sim", "y"):
            spinner("Abrindo imagem…")
            tentar_abrir(caminho)
        return

    if ext in (".mcpack", ".mcaddon", ".mcworld"):
        print(f"{G}  Pacote Minecraft.{D}")
        if input(f"{C}  Abrir/instalar? (s/n) → {W}").strip().lower() in ("s", "sim", "y"):
            spinner("Abrindo…")
            tentar_abrir(caminho)
        return

    if input(f"{C}  Abrir este arquivo? (s/n) → {W}").strip().lower() in ("s", "sim", "y"):
        spinner("Abrindo…")
        tentar_abrir(caminho)

def tentar_abrir(caminho):
    try:
        subprocess.run(["termux-open", caminho], check=False)
        print(f"\n{G}  Enviado para o app padrão.{D}")
    except:
        try:
            subprocess.run(["xdg-open", caminho], check=False)
        except:
            print(f"\n{R}  Não foi possível abrir.{D}")
            print(f"{W}  Caminho: {caminho}{D}")
    input(f"\n{C}  ENTER para voltar{D}")

def menu_arquivo(nome):
    clear()
    print(f"{C}  ╭────────────────────────────────────╮")
    print(f"{C}  │  ARQUIVO SELECIONADO               │")
    print(f"{C}  ╰────────────────────────────────────╯{D}\n")
    print(f"{W}  Arquivo: {Y}{nome}{D}\n")
    print(f"{G}  1. Abrir / Instalar{D}")
    print(f"{Y}  2. Mover (recortar){D}")
    print(f"{W}  3. Cancelar{D}")
    return input(f"\n{C}  → {W}").strip()

def welcome():
    clear()
    print(f"{C}")
    print("  ╭────────────────────────────────────╮")
    print("  │                                    │")
    print("  │     📁  EXPLORADOR DE ARQUIVOS     │")
    print("  │                                    │")
    print("  │         Healing_Boy85              │")
    print("  │                                    │")
    print("  ╰────────────────────────────────────╯")
    print(f"{D}")
    time.sleep(0.25)
    type_effect(f"{G}  Bem-vindo ao Explorador!{D}", 0.03)
    time.sleep(0.15)
    type_effect(f"{Y}  Criar • Mover • Renomear • .HB{D}", 0.022)
    print()
    input(f"{C}  ENTER para avançar…{D}")

def main():
    ensure_permissions()   # só pede se realmente precisar
    welcome()

    atual = get_start_path()
    historico = []
    clipboard = None

    while True:
        clear()
        desenhar_borda(atual, clipboard)

        dirs, files, erro = listar(atual)

        if erro:
            print(f"\n{R}  ⚠  {erro}{D}\n")
        else:
            print()
            if dirs:
                print(f"{G}  📂  PASTAS ({len(dirs)}){D}")
                for i, d in enumerate(dirs, 1):
                    print(f"  {G}{i:2d}.{D}  📁  {W}{d}{D}")
            if files:
                print(f"\n{Y}  📄  ARQUIVOS ({len(files)}){D}")
                base = len(dirs)
                for i, f in enumerate(files, 1):
                    print(f"  {Y}{base+i:2d}.{D}  📄  {W}{f}{D}")
            if not dirs and not files:
                print(f"\n{M}  (Vazio){D}")

        print(f"\n{C}  ──────────────────────────────────────{D}")
        print(f"{W}  [nº] Abrir   [n] Nova   [r] Renomear{D}")
        print(f"{W}  [v] Voltar   [q] Sair{D}", end="")
        if clipboard:
            print(f"   {M}[p] Colar{D}")
        else:
            print()

        try:
            escolha = input(f"{C}  └─> {W}").strip().lower()
        except (EOFError, KeyboardInterrupt):
            break

        if escolha in ("q", "sair", "exit"):
            clear()
            print(f"\n{G}  Até logo! — Healing_Boy85{D}\n")
            time.sleep(0.6)
            break

        if escolha in ("v", "voltar", "back"):
            if historico:
                spinner("Voltando…", 0.65)
                atual = historico.pop()
            else:
                print(f"\n{Y}  Já está na raiz.{D}")
                time.sleep(0.9)
            continue

        if escolha in ("n", "nova", "new"):
            criar_pasta(atual)
            continue

        if escolha in ("r", "renomear", "rename"):
            renomear_arquivo(atual, files)
            continue

        if escolha in ("p", "colar", "paste") and clipboard:
            clipboard = mover_aqui(atual, clipboard)
            continue

        if escolha.isdigit():
            idx = int(escolha) - 1
            todos = [(d, True) for d in dirs] + [(f, False) for f in files]
            if 0 <= idx < len(todos):
                nome, eh_pasta = todos[idx]
                full = os.path.join(atual, nome)

                if eh_pasta:
                    historico.append(atual)
                    atual = full
                    spinner(f"Abrindo {nome}…", 0.7)
                else:
                    op = menu_arquivo(nome)
                    if op == "1":
                        abrir_arquivo(full)
                    elif op == "2":
                        clipboard = full
                        print(f"\n{M}  ✂️  “{nome}” marcado para mover.{D}")
                        print(f"{W}  Vá até a pasta destino e digite {M}p{D}")
                        time.sleep(1.4)
            else:
                print(f"\n{R}  Número inválido.{D}")
                time.sleep(0.9)
        else:
            print(f"\n{R}  Opção não reconhecida.{D}")
            time.sleep(0.8)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear()
        print(f"\n{Y}  Encerrado.{D}\n")
EOF
python3 explorador.py
