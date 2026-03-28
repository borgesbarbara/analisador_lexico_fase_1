import sys
from funcao import *

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py entrada.txt")
        return

    linhas = lerArquivo(sys.argv[1])
    if linhas is None:
        return

    resultados = []

    for linha in linhas:
        try:
            tokens = parseExpressao(linha)

            resultado = executarExpressao(tokens)
            resultados.append(resultado)

            asm = gerarAssembly(tokens)

            print("\n--- Assembly ---")
            print(asm)

        except Exception as e:
            print("Erro:", e)

    exibirResultados(resultados)


if __name__ == "__main__":
    main()
