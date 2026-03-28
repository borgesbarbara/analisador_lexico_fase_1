#aluna:Bárbara batista Borges
#Grupo: grupo 21

import sys
from funcao import *

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py entrada1.txt entrada2.txt")
        return

    arquivos = sys.argv[1:]

    resultados = []
    tokens_gerados = []
    assemblies = []

    for nome_arquivo in arquivos:
        linhas = lerArquivo(nome_arquivo)

        if linhas is None:
            continue

        for linha in linhas:
            linha = linha.strip()

            if not linha:
                continue

            try:
                tokens = parseExpressao(linha)
                tokens_gerados.append(" ".join(tokens))
            except Exception as e:
                print("Erro (parse):", e)
                continue

            try:
                resultado = executarExpressao(tokens)
                resultados.append(resultado)
            except Exception as e:
                print("Erro (execução):", e)
                continue

            try:
                asm = gerarAssembly(tokens)
                assemblies.append(asm)
            except Exception as e:
                print("Erro (assembly):", e)

    salvarAssembly("saida.asm", assemblies)
    salvarTokens("tokens.txt", tokens_gerados)

    exibirResultados(resultados)


if __name__ == "__main__":
    main()
