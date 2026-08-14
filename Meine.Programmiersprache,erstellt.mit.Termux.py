cat << 'EOF' > bixo.py
import os, sys

t = {
    "1":"Q","2":"W","3":"E","4":"R","5":"T","6":"Y","7":"U","8":"I","9":"O","0":"P",
    "@":"A","#":"S","$":"D","_":"F","&":"G","+":"H","(":"J",")":"K","/":"L","*":"Z",
    "\"":"X",":":"V",";":"B","!":"N","?":"M","-":" ","¿":"?","[":"!",
    "<":",",">":".","\xb0":"-","‰":"%","≠":"=","±":"+","×":"*",
    "£":"Ã","§":"Õ","©":"Ç","€":"É","Ö":"Ô","Ø":"Ó","Į":"Í",
    "⁹":"1","⁸":"2","⁷":"3","⁶":"4","⁵":"5","⁴":"6","³":"7","²":"8","¹":"9","⁰":"0",
    "«":",",  
    "®":"'"   
}
ti = {v: k for k, v in t.items()}

def processar(linhas, dicionario):
    resultado = []
    for linha in linhas:
        if linha.strip() == "":
            resultado.append("")
        else:
            res = "".join([dicionario.get(char.upper() if dicionario == ti else char, char) for char in linha])
            resultado.append(res)
    return resultado

def mostrar_resultado(lista_res, cor, titulo):
    os.system("clear")
    largura = 31
    print(f"{cor}  ◢◤  {titulo}  ◥◣")
    print(f"{cor}  ┏" + "━"*largura + "┓")
    for l in lista_res:
        print(f"{cor}  ┃ \033[1;37m{l}")
    print(f"{cor}  ┗" + "━"*largura + "┛")
    print("\n" + "\n".join(lista_res))
    input(f"\n{cor}  [ ENTER PARA VOLTAR ]")

def mostrar_significados():
    os.system("clear")
    cyan = "\033[1;36m"
    white = "\033[1;37m"
    
    print(f"{cyan}  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    print(f"  ▓ {white}𖤓 MOD_SIGNIFICADO v1.2 𖤓 {cyan}▓")
    print(f"  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\033[0m\n")
    
    print(f"{cyan}  ══╦【 ALFABETO DE A A Z 】╦══")
    print(f"{white}  ║  @ = A  │  ( = J  │  1 = Q  │  \" = X")
    print(f"  ║  ; = B  │  ) = K  │  4 = R  │  6 = Y")
    print(f"  ║  ' = C  │  / = L  │  # = S  │  * = Z")
    print(f"  ║  $ = D  │  ? = M  │  5 = T")
    print(f"  ║  3 = E  │  ! = N  │  7 = U")
    print(f"  ║  _ = F  │  9 = O  │  : = V")
    print(f"  ║  & = G  │  0 = P  │  2 = W")
    print(f"  ║  + = H")
    print(f"  ║  8 = I")
    
    print(f"\n{cyan}  ══╦【 NÚMEROS E ACENTOS 】╦══")
    print(f"{white}  ║  ⁹=1 │ ⁸=2 │ ⁷=3 │ ⁶=4 │ ⁵=5")
    print(f"  ║  ⁴=6 │ ³=7 │ ²=8 │ ¹=9 │ ⁰=0")
    print(f"  ║  £=Ã │ §=Õ │ ©=Ç │ €=É │ Ö=Ô")
    print(f"  ║  Ø=Ó │ Į=Í")
    
    print(f"\n{cyan}  ══╦【 PONTUAÇÃO E SINAIS 】╦══")
    print(f"{white}  ║  - = [Espaço]   │  ¿ = ?")
    print(f"  ║  [ = !          │  < = ,")
    print(f"  ║  > = .          │  ° = -")
    print(f"  ║  ‰ = %          │  « = , (Vírgula)")
    print(f"  ║  ▼ = =          │  ® = ' (Apóstrofo)")
    print(f"  ║  ± = +          │  × = *")
    
    print(f"\n{cyan}  ╚═══════════════════════════════╝")
    input(f"\n{cyan}  [ ENTER PARA VOLTAR AO MENU ]\033[0m")

modo_inverso = False
while True:
    os.system("clear")
    cor_menu = "\033[1;31m" if modo_inverso else "\033[1;32m"
    print(f"{cor_menu}  ╔" + "═"*35 + "╗")
    print(f"  {cor_menu}║ \033[1;37m BY: HEALING_BOY85   \033[1;30m| \033[1;32mv10.6 {cor_menu}║")
    print(f"  {cor_menu}║ \033[1;30m [✦]Trocar [♰]Criação [𖤓]Significa  {cor_menu}║")
    print(f"{cor_menu}  ╚" + "═"*35 + "╝\033[0m")
    try:
        msg = input(f"\n{cor_menu}  └─> \033[1;37m")
    except EOFError: break
    if msg.upper() == "SAIR": break
    if msg == "✦":
        modo_inverso = not modo_inverso
        continue
    if msg == "𖤓" or msg.upper() == "SIGNIFICA":
        mostrar_significados()
        continue
    if msg == "♰":
        while True:
            os.system("clear")
            cor_menu = "\033[1;31m" if modo_inverso else "\033[1;32m"
            tit_tela = "MODO CRIAÇÃO" if modo_inverso else "MODO TRADUÇÃO"
            print(f"{cor_menu}  ◢◤  {tit_tela}  ◥◣")
            print(f"\033[1;30m  (Cole o texto com parágrafos e dê CTRL+D)\n  (Ou digite APENAS ✦ para inverter ou ♰ para voltar)\n\033[1;37m")
            try:
                entrada_longa = sys.stdin.read().splitlines()
            except EOFError: break
            
            if not entrada_longa:
                continue
                
            if len(entrada_longa) == 1 and entrada_longa[0].strip() in ["✦", "♰"]:
                cmd = entrada_longa[0].strip()
                if cmd == "✦":
                    modo_inverso = not modo_inverso
                    continue
                if cmd == "♰":
                    break
            
            res_lista = processar(entrada_longa, ti if modo_inverso else t)
            mostrar_resultado(res_lista, cor_menu, "SUCESSO")
        continue
        
    if msg.strip() != "":
        res_lista = processar([msg], ti if modo_inverso else t)
        mostrar_resultado(res_lista, cor_menu, "RESPOSTA")
EOF
python bixo.py
