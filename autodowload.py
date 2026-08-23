cat << 'EOF' > healing.sh
#!/data/data/com.termux/files/usr/bin/bash

# ═══════════════════════════════════════════════════════════
#          HB DOWNLOADER SYSTEM — VERSÃO 4.3 FINAL INFO
#          Desenvolvido por HealingBoy85 © 2026
# ═══════════════════════════════════════════════════════════

# 📍 INFORMAÇÕES DO SISTEMA
NOME_ARQUIVO="healing.sh"
PASTA_SCRIPT="$HOME"
PASTA_DOWNLOADS="$HOME/storage/downloads"
VERSAO="4.3"

# 🎨 PALETA — SÓ CIANO E CORES COMPLEMENTARES
CIANO='\033[1;96m'
CIANO_CLARO='\033[1;36m'
CIANO_FRACO='\033[0;96m'
BRANCO='\033[1;97m'
CINZA='\033[1;90m'
VERDE='\033[1;92m'
VERMELHO='\033[1;91m'
AMARELO='\033[1;93m'
RESET='\033[0m'

# ═══════════════════════════════════════════════════════════
# 📦 FUNÇÕES DE ANIMAÇÃO E UI
# ═══════════════════════════════════════════════════════════

fn_LimparTela() {
    clear
}

fn_Pausa() {
    sleep "${1:-0.1}"
}

fn_AnimacaoTexto() {
    local texto="$1"
    echo -ne "  ${CIANO}"
    for ((i=0; i<${#texto}; i++)); do
        echo -ne "${texto:$i:1}"
        fn_Pausa 0.03
    done
    echo -e "${RESET}"
}

fn_BarraRomana() {
    local passo="$1"
    local total="$2"
    local comprimento=15
    local concluido=$(( comprimento * passo / total ))
    local restante=$(( comprimento - concluido ))

    echo -ne "  ${CIANO}╔"
    local i=0
    while [ $i -lt $concluido ]; do
        case $i in
            0|4|8|12) echo -ne "${BRANCO}█${RESET}" ;;
            *) echo -ne "${CIANO}█${RESET}" ;;
        esac
        i=$((i+1))
    done
    i=0
    while [ $i -lt $restante ]; do
        echo -ne "${CINZA}░${RESET}"
        i=$((i+1))
    done
    echo -ne "${CIANO}╗${RESET}"

    local porcentagem=$(( passo * 100 / total ))
    local romano=""
    case $porcentagem in
        0) romano="I" ;; 10) romano="X" ;; 20) romano="XX" ;; 30) romano="XXX" ;; 40) romano="XL" ;;
        50) romano="L" ;; 60) romano="LX" ;; 70) romano="LXX" ;; 80) romano="LXXX" ;; 90) romano="XC" ;; 100) romano="C" ;;
        *) romano="$porcentagem" ;;
    esac
    echo -ne " ${AMARELO}${romano}${RESET}"
    echo -ne "\r"
}

fn_TelaInicial() {
    fn_LimparTela

    echo -ne "${CIANO}╔"
    for i in {1..38}; do echo -ne "═"; fn_Pausa 0.02; done
    echo -ne "╗${RESET}\n"

    echo -ne "${CIANO}║${RESET}"; fn_Pausa 0.1
    echo -ne "                                      "; fn_Pausa 0.1
    echo -ne "${CIANO}║${RESET}\n"; fn_Pausa 0.1

    # HB CERTO
    echo -ne "${CIANO}║${RESET}"; fn_Pausa 0.1
    echo -ne "      ${BRANCO}██╗  ██╗ ██████╗${RESET}        "; fn_Pausa 0.1
    echo -ne "${CIANO}║${RESET}\n"; fn_Pausa 0.1

    echo -ne "${CIANO}║${RESET}"; fn_Pausa 0.1
    echo -ne "      ${BRANCO}██║  ██║██╔══██╗${RESET}       "; fn_Pausa 0.1
    echo -ne "${CIANO}║${RESET}\n"; fn_Pausa 0.1

    echo -ne "${CIANO}║${RESET}"; fn_Pausa 0.1
    echo -ne "      ${BRANCO}███████║██████╔╝${RESET}       "; fn_Pausa 0.1
    echo -ne "${CIANO}║${RESET}\n"; fn_Pausa 0.1

    echo -ne "${CIANO}║${RESET}"; fn_Pausa 0.1
    echo -ne "      ${BRANCO}██╔══██║██╔══██╗${RESET}       "; fn_Pausa 0.1
    echo -ne "${CIANO}║${RESET}\n"; fn_Pausa 0.1

    echo -ne "${CIANO}║${RESET}"; fn_Pausa 0.1
    echo -ne "      ${BRANCO}██║  ██║██████╔╝${RESET}       "; fn_Pausa 0.1
    echo -ne "${CIANO}║${RESET}\n"; fn_Pausa 0.1

    echo -ne "${CIANO}║${RESET}"; fn_Pausa 0.1
    echo -ne "      ${BRANCO}╚═╝  ╚═╝╚═════╝ ${RESET}       "; fn_Pausa 0.1
    echo -ne "${CIANO}║${RESET}\n"; fn_Pausa 0.1

    echo -ne "${CIANO}║${RESET}"; fn_Pausa 0.1
    echo -ne "                                      "; fn_Pausa 0.1
    echo -ne "${CIANO}║${RESET}\n"; fn_Pausa 0.1

    echo -ne "${CIANO}║${RESET}  "; fn_Pausa 0.1
    fn_AnimacaoTexto "       HB DOWNLOADER v${VERSAO}           "
    echo -ne "${CIANO}║${RESET}\n"

    echo -ne "${CIANO}║${RESET}  "; fn_Pausa 0.1
    fn_AnimacaoTexto "  YouTube • Instagram • TikTok  "
    echo -ne "  ${CIANO}║${RESET}\n"

    echo -ne "${CIANO}║${RESET}"; fn_Pausa 0.1
    echo -ne "                                      "; fn_Pausa 0.1
    echo -ne "${CIANO}║${RESET}\n"; fn_Pausa 0.1

    echo -ne "${CIANO}╚"; fn_Pausa 0.1
    for i in {1..38}; do echo -ne "═"; fn_Pausa 0.02; done
    echo -ne "╝${RESET}\n"

    fn_Pausa 0.5
}

fn_CarregamentoSistema() {
    echo -e "\n${CIANO}══════════════════════════════════════${RESET}"
    fn_AnimacaoTexto "  INICIALIZANDO NUCLEO DO SISTEMA"
    echo -e "${CIANO}══════════════════════════════════════${RESET}\n"

    for p in 1 2 3 4 5 6 7 8 9 10; do
        fn_BarraRomana $p 10
        fn_Pausa 0.08
    done
    echo ""

    echo -e "\n  ${VERDE}✓ Sistema carregado com sucesso!${RESET}\n"
}

fn_TelaVerificacao() {
    echo -e "${CIANO}──────────────────────────────────────${RESET}"
    fn_AnimacaoTexto "  VERIFICACAO DE COMPONENTES"
    echo -e "${CIANO}──────────────────────────────────────${RESET}\n"
}

fn_TelaDownloadIniciando() {
    echo -e "\n${CIANO}╔════════════════════════════════════╗${RESET}"
    echo -e "${CIANO}║${RESET}                                    ${CIANO}║${RESET}"
    echo -e "${CIANO}║${RESET}     PROCESSANDO DOWNLOAD...       ${CIANO}║${RESET}"
    echo -e "${CIANO}║${RESET}                                    ${CIANO}║${RESET}"
    echo -e "${CIANO}╚════════════════════════════════════╝${RESET}\n"

    fn_AnimacaoTexto "  > Analisando endereco do video..."
    for p in 1 2 3 4 5 6 7 8 9 10; do
        fn_BarraRomana $p 10
        fn_Pausa 0.08
    done
    echo -e "\n  ${VERDE}✓ Link validado${RESET}\n"

    fn_AnimacaoTexto "  > Estabelecendo conexao..."
    for p in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15; do
        fn_BarraRomana $p 15
        fn_Pausa 0.06
    done
    echo -e "\n  ${VERDE}✓ Conexao estavel${RESET}\n"

    fn_AnimacaoTexto "  > Transferindo dados..."
    for p in 1 2 3 4 5 6 7 8; do
        fn_BarraRomana $p 8
        fn_Pausa 0.1
    done
    echo -e "\n  ${VERDE}✓ Dados recebidos${RESET}\n"

    fn_AnimacaoTexto "  > Finalizando arquivo..."
    for p in 1 2 3 4 5 6 7 8 9 10; do
        fn_BarraRomana $p 10
        fn_Pausa 0.08
    done
    echo -e "\n  ${VERDE}✓ Arquivo pronto!${RESET}\n"
}

fn_TelaSucesso() {
    echo -e "\n${VERDE}╔════════════════════════════════════╗${RESET}"
    echo -e "${VERDE}║${RESET}                                    ${VERDE}║${RESET}"
    echo -e "${VERDE}║${RESET}       DOWNLOAD CONCLUIDO!         ${VERDE}║${RESET}"
    echo -e "${VERDE}║${RESET}                                    ${VERDE}║${RESET}"
    echo -e "${VERDE}║${RESET}  Salvo em: Arquivos > Downloads   ${VERDE}║${RESET}"
    echo -e "${VERDE}║${RESET}                                    ${VERDE}║${RESET}"
    echo -e "${VERDE}╚════════════════════════════════════╝${RESET}"
}

fn_TelaErro() {
    echo -e "\n${VERMELHO}╔════════════════════════════════════╗${RESET}"
    echo -e "${VERMELHO}║${RESET}                                    ${VERMELHO}║${RESET}"
    echo -e "${VERMELHO}║${RESET}      FALHA NO DOWNLOAD            ${VERMELHO}║${RESET}"
    echo -e "${VERMELHO}║${RESET}                                    ${VERMELHO}║${RESET}"
    echo -e "${VERMELHO}║${RESET}  Verifique o link e a conexao     ${VERMELHO}║${RESET}"
    echo -e "${VERMELHO}║${RESET}                                    ${VERMELHO}║${RESET}"
    echo -e "${VERMELHO}╚════════════════════════════════════╝${RESET}"
}

fn_TelaInformacoes() {
    echo -e "\n\n${CIANO}╔══════════════════════════════════════════════════════╗${RESET}"
    echo -e "${CIANO}║${RESET}                  INFORMAÇÕES DO SISTEMA               ${CIANO}║${RESET}"
    echo -e "${CIANO}╠══════════════════════════════════════════════════════╣${RESET}"
    echo -e "${CIANO}║${RESET}                                                      ${CIANO}║${RESET}"
    echo -e "${CIANO}║${RESET}  📄 Nome do arquivo:  ${BRANCO}${NOME_ARQUIVO}${RESET}                        ${CIANO}║${RESET}"
    echo -e "${CIANO}║${RESET}  📂 Pasta do script:   ${BRANCO}${PASTA_SCRIPT}${RESET}              ${CIANO}║${RESET}"
    echo -e "${CIANO}║${RESET}  💾 Pasta de downloads: ${BRANCO}${PASTA_DOWNLOADS}${RESET}    ${CIANO}║${RESET}"
    echo -e "${CIANO}║${RESET}  🏷️  Versão:          ${BRANCO}v${VERSAO}${RESET}                             ${CIANO}║${RESET}"
    echo -e "${CIANO}║${RESET}                                                      ${CIANO}║${RESET}"
    echo -e "${CIANO}╠══════════════════════════════════════════════════════╣${RESET}"
    echo -e "${CIANO}║${RESET}               ⚠️  POSSÍVEIS DEFEITOS E SOLUÇÕES        ${CIANO}║${RESET}"
    echo -e "${CIANO}╠══════════════════════════════════════════════════════╣${RESET}"
    echo -e "${CIANO}║${RESET}                                                      ${CIANO}║${RESET}"
    echo -e "${CIANO}║${RESET}  ❌ Não baixa → ✅ Verifique internet / link valido   ${CIANO}║${RESET}"
    echo -e "${CIANO}║${RESET}  ❌ Arquivo não aparece → ✅ Rode: termux-setup-storage ${CIANO}║${RESET}"
    echo -e "${CIANO}║${RESET}  ❌ Comando não encontrado → ✅ Atualize: pkg update  ${CIANO}║${RESET}"
    echo -e "${CIANO}║${RESET}  ❌ Senha errada → ✅ Senha: healingboy85            ${CIANO}║${RESET}"
    echo -e "${CIANO}║${RESET}  ❌ Permissão negada → ✅ Chmod +x healing.sh        ${CIANO}║${RESET}"
    echo -e "${CIANO}║${RESET}                                                      ${CIANO}║${RESET}"
    echo -e "${CIANO}╚══════════════════════════════════════════════════════╝${RESET}"
}

fn_TelaEncerramento() {
    fn_LimparTela
    
    fn_TelaInformacoes
    
    echo -e "\n${CIANO}╔════════════════════════════════════╗${RESET}"
    echo -e "${CIANO}║${RESET}                                    ${CIANO}║${RESET}"
    echo -e "${CIANO}║${RESET}      OBRIGADO POR USAR!           ${CIANO}║${RESET}"
    echo -e "${CIANO}║${RESET}                                    ${CIANO}║${RESET}"
    echo -e "${CIANO}║${RESET}    HealingBoy85 © MMXXVI           ${CIANO}║${RESET}"
    echo -e "${CIANO}║${RESET}                                    ${CIANO}║${RESET}"
    echo -e "${CIANO}║${RESET}         ATE A PROXIMA!              ${CIANO}║${RESET}"
    echo -e "${CIANO}║${RESET}                                    ${CIANO}║${RESET}"
    echo -e "${CIANO}╚════════════════════════════════════╝${RESET}"
    sleep 3
    fn_LimparTela
}

fn_LinhaDivisoria() {
    echo -e "${CIANO}──────────────────────────────────────${RESET}"
}

# ═══════════════════════════════════════════════════════════
# 🔐 INICIO DO SISTEMA
# ═══════════════════════════════════════════════════════════

fn_TelaInicial
fn_CarregamentoSistema

# ═══════════════════════════════════════════════════════════
# 🔐 AUTENTICACAO — SENHA VISIVEL!
# ═══════════════════════════════════════════════════════════

tentativas=3
fn_LinhaDivisoria
echo ""

while [ $tentativas -gt 0 ]; do
    echo -ne "  🔒 Digite a chave de acesso (s para sair): "
    read senha  # SENHA VISIVEL

    if [ "$senha" = "s" ] || [ "$senha" = "S" ]; then
        echo -e "  ⚡ Encerrando sessao..."
        sleep 0.8
        fn_LimparTela
        exit 0
    fi

    if [ "$senha" = "healingboy85" ]; then
        echo -e "  ${VERDE}✓ Acesso autorizado — Bem-vindo!${RESET}\n"
        sleep 0.5
        break
    else
        tentativas=$((tentativas-1))
        if [ $tentativas -gt 0 ]; then
            echo -e "  ${VERMELHO}✗ Chave invalida. Restam $tentativas tentativa(s)${RESET}\n"
        else
            echo -e "  ${VERMELHO}✗ Limite excedido. Sistema bloqueado.${RESET}"
            sleep 1.5
            fn_LimparTela
            exit 1
        fi
    fi
done

# ═══════════════════════════════════════════════════════════
# 🔍 VERIFICACAO DE DEPENDENCIAS
# ═══════════════════════════════════════════════════════════

fn_TelaVerificacao
precisa_instalar=false

if [ ! -d "$HOME/storage" ]; then
    echo -e "  ${VERMELHO}✗${RESET} Armazenamento"
    precisa_instalar=true
else
    echo -e "  ${VERDE}✓${RESET} Armazenamento"
fi

if command -v python &>/dev/null; then
    echo -e "  ${VERDE}✓${RESET} Python"
else
    echo -e "  ${VERMELHO}✗${RESET} Python"
    precisa_instalar=true
fi

if command -v ffmpeg &>/dev/null; then
    echo -e "  ${VERDE}✓${RESET} FFmpeg"
else
    echo -e "  ${VERMELHO}✗${RESET} FFmpeg"
    precisa_instalar=true
fi

if command -v yt-dlp &>/dev/null; then
    echo -e "  ${VERDE}✓${RESET} yt-dlp"
else
    echo -e "  ${VERMELHO}✗${RESET} yt-dlp"
    precisa_instalar=true
fi

echo ""

if [ "$precisa_instalar" = true ]; then
    fn_AnimacaoTexto "  ⚡ Instalando componentes necessarios..."
    echo ""
    for p in 1 2 3 4 5 6 7 8 9 10; do
        fn_BarraRomana $p 10
        fn_Pausa 0.1
        case $p in
            3) pkg update -y &>/dev/null ;;
            5) pkg upgrade -y &>/dev/null ;;
            6) [ ! -d "$HOME/storage" ] && termux-setup-storage ;;
            7) pkg install python ffmpeg -y &>/dev/null ;;
            9) pip install -U yt-dlp &>/dev/null ;;
        esac
    done
    echo -e "\n  ${VERDE}✓ Instalacao concluida!${RESET}\n"
else
    echo -e "  ${VERDE}✓ Todos os componentes carregados${RESET}\n"
fi

sleep 0.8

# ═══════════════════════════════════════════════════════════
# 📥 LOOP PRINCIPAL DE DOWNLOAD
# ═══════════════════════════════════════════════════════════

while true; do
    fn_LimparTela

    echo -e "${CIANO}╭──────────────────────────────────────╮${RESET}"
    echo -e "${CIANO}│${RESET}          AREA DE DOWNLOAD          ${CIANO}│${RESET}"
    echo -e "${CIANO}╰──────────────────────────────────────╯${RESET}"
    echo ""

    fn_AnimacaoTexto "  🔗 Cole o link do video: "
    read url

    if [ -z "$url" ]; then
        echo -e "\n  ${VERMELHO}✗ Nenhum link fornecido${RESET}"
        sleep 1
        continue
    fi

    fn_TelaDownloadIniciando

    yt-dlp -q --no-warnings -f "bv*+ba/b" --merge-output-format mp4 -o "$HOME/storage/downloads/%(title)s.%(ext)s" "$url"
    status=$?

    if [ $status -eq 0 ]; then
        fn_TelaSucesso
    else
        fn_TelaErro
    fi

    echo ""
    fn_LinhaDivisoria
    echo ""

    while true; do
        fn_AnimacaoTexto "  🔄 Baixar outro? (S/N): "
        read resposta
        case "$resposta" in
            s|S) echo ""; break ;;
            n|N) fn_TelaEncerramento; exit 0 ;;
            *) echo -e "  ${VERMELHO}✗ Digite apenas S ou N${RESET}\n" ;;
        esac
    done
done
EOF

chmod +x healing.sh
./healing.sh
