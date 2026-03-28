import math


#aluno 1
def estadoNumero(s):
    if not s:
        return False

    tem_ponto = False

    for c in s:
        if c.isdigit():
            continue
        elif c == '.':
            if tem_ponto:
                return False
            tem_ponto = True
        else:
            return False

    return True


def estadoOperador(s):
    return s in ["+", "-", "*", "/", "//", "%", "^"]


def estadoComando(s):
    return s in ["MEM", "RES"]


def parseExpressao(linha):
    tokens = linha.split()

    for t in tokens:
        if not (estadoNumero(t) or estadoOperador(t) or estadoComando(t)):
            raise Exception(f"Token inválido: {t}")

    return tokens


#aluno 2
memoria = {"MEM": 0.0}
historico = []

def executarExpressao(tokens):
    pilha = []

    for t in tokens:

        if estadoNumero(t):
            pilha.append(float(t))

        elif estadoOperador(t):
            if len(pilha) < 2:
                raise Exception("Expressão inválida")

            b = pilha.pop()
            a = pilha.pop()

            if t == "+":
                pilha.append(a + b)
            elif t == "-":
                pilha.append(a - b)
            elif t == "*":
                pilha.append(a * b)
            elif t == "/":
                pilha.append(a / b)
            elif t == "//":
                pilha.append(math.floor(a / b))
            elif t == "%":
                pilha.append(a % b)
            elif t == "^":
                pilha.append(a ** b)

        elif t == "MEM":
            if pilha:
                memoria["MEM"] = pilha.pop()
            else:
                pilha.append(memoria["MEM"])

        elif t == "RES":
            if pilha:
                n = int(pilha.pop())
                if n <= len(historico):
                    pilha.append(historico[-n])
            else:
                if historico:
                    pilha.append(historico[-1])

    resultado = pilha[-1]
    historico.append(resultado)

    return resultado


######################################################
# ASSEMBLY (ALUNO 3)
######################################################

def gerarAssembly(tokens):
    asm = ""
    pilha = []
    reg = 0

    for t in tokens:

        if estadoNumero(t):
            r = f"R{reg}"
            reg += 1
            asm += f"MOV {r}, #{t}\n"
            pilha.append(r)

        elif estadoOperador(t):
            b = pilha.pop()
            a = pilha.pop()

            if t == "+":
                asm += f"ADD {a}, {a}, {b}\n"
            elif t == "-":
                asm += f"SUB {a}, {a}, {b}\n"
            elif t == "*":
                asm += f"MUL {a}, {a}, {b}\n"
            elif t in ["/", "//"]:
                asm += f"SDIV {a}, {a}, {b}\n"
            elif t == "%":
                asm += f"SDIV R12, {a}, {b}\n"
                asm += f"MUL R12, R12, {b}\n"
                asm += f"SUB {a}, {a}, R12\n"

            pilha.append(a)

        elif t == "MEM":
            r = pilha.pop()
            asm += "LDR R10, =MEMORIA\n"
            asm += f"STR {r}, [R10]\n"

        elif t == "RES":
            r = f"R{reg}"
            reg += 1
            asm += "LDR R11, =RESULTADO\n"
            asm += f"LDR {r}, [R11]\n"
            pilha.append(r)

    if pilha:
        r = pilha[-1]
        asm += "LDR R11, =RESULTADO\n"
        asm += f"STR {r}, [R11]\n"
        
    
    

    return asm


######################################################
# ARQUIVO (ALUNO 3)
######################################################

def lerArquivo(nome):
    try:
        with open(nome, "r") as f:
            linhas = [linha.strip() for linha in f if linha.strip()]
        return linhas
    except:
        print("Erro ao abrir arquivo.")
        return None


######################################################
# OUTPUT (ALUNO 4)
######################################################

def exibirResultados(resultados):
    print("\n===== RESULTADOS =====")
    for i, r in enumerate(resultados):
        print(f"Expr {i+1}: {r:.1f}")

def salvarAssembly(nome_arquivo, lista_assembly):
    with open(nome_arquivo, "w") as f:
        for bloco in lista_assembly:
            f.write(bloco)
            f.write("\n")
