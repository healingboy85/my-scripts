cat << 'EOF' > healing.sh
#!/data/data/com.termux/files/usr/bin/bash

G='\033[1;32m'
R='\033[1;31m'
C='\033[1;36m'
Y='\033[1;33m'
W='\033[1;37m'
NC='\033[0m'

clear

# ===== RAPOSA =====
echo -e "${Y}"
echo "            /\\_/\\"
echo "           ( o.o )"
echo "            > ^ <"
echo -e "${NC}"

# ===== CABEÇALHO =====
echo -e "${G}"
echo "  ╔════════════════════════════════╗"
echo "  ║                                ║"
echo "  ║       by HealingBoy85          ║"
echo "  ║    VIDEO DOWNLOADER SYSTEM     ║"
echo "  ║           v2.3                 ║"
echo "  ║                                ║"
echo "  ╚════════════════════════════════╝"
echo -e "${NC}"
echo -e "  \( {C}YouTube • Instagram • TikTok \){NC}"
echo ""

# ===== SENHA =====
tentativas=3

while [ $tentativas -gt 0 ]; do
    echo -ne "  ${Y}[?] Senha (ou s pra sair): ${NC}"
    read senha
    echo ""

    if [ "$senha" = "s" ] || [ "$senha" = "S" ]; then
        echo -e "  \( {R}[!] Saindo... \){NC}"
        sleep 1
        clear
        exit 0
    fi

    if [ "$senha" = "tarobinha" ]; then
        echo -e "  \( {G}[✓] Acesso autorizado! \){NC}"
        sleep 0.7
        break
    else
        tentativas=$((tentativas-1))
        if [ $tentativas -gt 0 ]; then
            echo -e "  ${R}[!] Senha errada. Restam \( tentativas chance(s) \){NC}"
            echo ""
        else
            echo -e "  \( {R}[!] 3 erros. Sistema bloqueado. \){NC}"
            sleep 1.5
            clear
            exit 1
        fi
    fi
done

echo ""
echo -e "  \( {C}────────────────────────────── \){NC}"
echo ""

# ===== VERIFICAÇÃO =====
echo -e "  \( {C}[*] Verificando sistema... \){NC}"

# Carregamento falso
echo -ne "  ${C}[*] Carregando"
for i in 1 2 3 4 5; do
    echo -ne "."
    sleep 0.25
done
echo -e "${NC}"
echo ""

precisa=false

if [ ! -d "$HOME/storage" ]; then
    echo -e "  \( {Y}[!] Storage não configurado \){NC}"
    precisa=true
fi

if ! command -v python >/dev/null 2>&1; then
    echo -e "  \( {Y}[!] Python não encontrado \){NC}"
    precisa=true
fi

if ! command -v ffmpeg >/dev/null 2>&1; then
    echo -e "  \( {Y}[!] FFmpeg não encontrado \){NC}"
    precisa=true
fi

if ! command -v yt-dlp >/dev/null 2>&1; then
    echo -e "  \( {Y}[!] yt-dlp não encontrado \){NC}"
    precisa=true
fi

if [ "$precisa" = true ]; then
    echo -e "  \( {C}[*] Instalando, aguarde... \){NC}"
    
    echo -ne "  ${C}[*] Progresso"
    for i in 1 2 3 4 5 6; do
        echo -ne "."
        sleep 0.3
    done
    echo -e "${NC}"
    
    pkg update -y && pkg upgrade -y > /dev/null 2>&1

    if [ ! -d "$HOME/storage" ]; then
        termux-setup-storage
        sleep 2
    fi

    pkg install python ffmpeg -y > /dev/null 2>&1
    pip install -U yt-dlp > /dev/null 2>&1

    echo -e "  \( {G}[✓] Instalação concluída! \){NC}"
else
    echo -e "  \( {G}[✓] Tudo pronto. \){NC}"
fi

echo ""
echo -e "  \( {C}────────────────────────────── \){NC}"
echo ""

# ===== LOOP DE DOWNLOAD =====
while true; do
    echo -e "  \( {W}    === ÁREA DE DOWNLOAD === \){NC}"
    echo ""

    echo -ne "  ${Y}[?] Cole o link: ${NC}"
    read url

    if [ -z "$url" ]; then
        echo -e "  \( {R}[!] Nenhum link informado. \){NC}"
        sleep 1
        continue
    fi

    echo ""
    echo -e "  \( {C}[*] Preparando download... \){NC}"
    
    # Carregamento falso
    echo -ne "  ${C}[*] Baixando"
    for i in 1 2 3 4 5 6 7; do
        echo -ne "."
        sleep 0.2
    done
    echo -e "${NC}"
    echo ""

    yt-dlp -f "bv*+ba/b" --merge-output-format mp4 -o "$HOME/storage/downloads/%(title)s.%(ext)s" "$url"
    status=$?

    echo ""

    if [ $status -eq 0 ]; then
        echo -e "  \( {G}╔════════════════════════════════╗ \){NC}"
        echo -e "  \( {G}║                                ║ \){NC}"
        echo -e "  \( {G}║     DOWNLOAD FINALIZADO        ║ \){NC}"
        echo -e "  \( {G}║         COM SUCESSO!           ║ \){NC}"
        echo -e "  \( {G}║                                ║ \){NC}"
        echo -e "  \( {G}╚════════════════════════════════╝ \){NC}"
        echo ""
        echo -e "  \( {C}[*] Arquivo salvo em: Download \){NC}"
    else
        echo -e "  \( {R}╔════════════════════════════════╗ \){NC}"
        echo -e "  \( {R}║                                ║ \){NC}"
        echo -e "  \( {R}║      ERRO NO DOWNLOAD          ║ \){NC}"
        echo -e "  \( {R}║     Tente outro link           ║ \){NC}"
        echo -e "  \( {R}║                                ║ \){NC}"
        echo -e "  \( {R}╚════════════════════════════════╝ \){NC}"
    fi

    echo ""
    echo -e "  \( {C}────────────────────────────── \){NC}"
    echo ""

    # Pergunta se quer baixar outro
    while true; do
        echo -ne "  ${Y}[?] Baixar outro vídeo? (s/n): ${NC}"
        read resposta

        if [ "$resposta" = "s" ] || [ "$resposta" = "S" ]; then
            echo ""
            echo -e "  \( {C}────────────────────────────── \){NC}"
            echo ""
            break
        elif [ "$resposta" = "n" ] || [ "$resposta" = "N" ]; then
            echo ""
            echo -e "  \( {G}╔════════════════════════════════╗ \){NC}"
            echo -e "  \( {G}║                                ║ \){NC}"
            echo -e "  \( {G}║         by HealingBoy85        ║ \){NC}"
            echo -e "  \( {G}║                                ║ \){NC}"
            echo -e "  \( {G}║      Obrigado por usar!        ║ \){NC}"
            echo -e "  \( {G}║                                ║ \){NC}"
            echo -e "  \( {G}╚════════════════════════════════╝ \){NC}"
            echo ""
            sleep 1.5
            clear
            exit 0
        else
            echo -e "  \( {R}[!] Digite apenas s ou n \){NC}"
            echo ""
        fi
    done
done
EOF
chmod +x healing.sh
./healing.sh
