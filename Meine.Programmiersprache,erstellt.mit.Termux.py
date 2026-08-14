cat << 'EOF' > bixo.py
import os, sys

t = {
    "1":"Q","2":"W","3":"E","4":"R","5":"T","6":"Y","7":"U","8":"I","9":"O","0":"P",
    "@":"A","#":"S","$":"D","_":"F","&":"G","+":"H","(":"J",")":"K","/":"L","*":"Z",
    "\"":"X","'":"C",":":"V",";":"B","!":"N","?":"M","-":" ","¿":"?","[":"!",
    "<":",",">":".","°":"-","‰":"%","≠":"=","±":"+","×":"*",
    "£":"Ã","§":"Õ","©":"Ç","€":"É","Ö":"Ô","Ø":"Ó","Į":"Í",
    "⁹":"1","⁸":"2","⁷":"3","⁶":"4","⁵":"5","⁴":"6","³":"7","²":"8","¹":"9","⁰":"0"
}
ti = {v: k for k, v in t.items()}

def processar(linhas, dicionario):
    resultado = []
    for linha in linhas:
        if linha.strip() == "":
            resultado.append("-" * 25)
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
    print("\n".join(lista_res))
    input(f"\n{cor}  [ ENTER ]")

modo_inverso = False
while True:
    os.system("clear")
    cor_menu = "\033[1;31m" if modo_inverso else "\033[1;32m"
    # Moldura ajustada com o novo nome HEALING_BOY85
    print(f"{cor_menu}  ╔" + "═"*31 + "╗")
    print(f"  {cor_menu}║ \033[1;37m BY: HEALING_BOY85 \033[1;30m| \033[1;32mv10.6 {cor_menu}║")
    print(f"  {cor_menu}║ \033[1;30m [✦]=Modo  | [♰]=Traduzir     {cor_menu}║")
    print(f"{cor_menu}  ╚" + "═"*31 + "╝\033[0m")
    try:
        msg = input(f"\n{cor_menu}  └─> \033[1;37m")
    except EOFError: break
    if msg.upper() == "SAIR": break
    if msg == "✦":
        modo_inverso = not modo_inverso
        continue
    if msg == "♰":
        while True:
            os.system("clear")
            print(f"{cor_menu}  ◢◤  PROCESSANDO  ◥◣\n")
            try:
                entrada_longa = sys.stdin.read().splitlines()
            except EOFError: break
            if entrada_longa:
                res_lista = processar(entrada_longa, ti if modo_inverso else t)
                mostrar_resultado(res_lista, cor_menu, "SUCESSO")
            break
        continue
    if msg.strip() != "":
        res_lista = processar([msg], ti if modo_inverso else t)
        mostrar_resultado(res_lista, cor_menu, "RESPOSTA")
EOF
python bixo.py
