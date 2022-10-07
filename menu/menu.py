import imp
import time
import data.popularBanco as popularBanco
import data.lerDados as lerDados
import _utils.definirCaminhos as caminho
import _utils.clearConsole as clearConsole

startTime = 0.0

def menu():
    clearConsole.Clear()
    print("Analisador de votos")
    print("-*-"*10)
    print("1 - Inserir dados")
    print("2 - Analisar dados")
    print("\n\t0 - Sair\n")

    opcao = int(input("Digite a opção desejada: "))
    if opcao == 0:
        exit()
    elif opcao == 1:
        clearConsole.Clear()
        startTime = time.time()
        popularBanco.popularBanco(caminho.LeituraCSV())
        print(f"Tempo de execução: {time.time() - startTime:.2f} segundos")
        input("Pressione qualquer tecla para continuar...")
    elif opcao == 2:
        clearConsole.Clear()
        startTime = time.time()
        lerDados.LerDados()
        print(f"Tempo de execução: {time.time() - startTime:.2f} segundos")
        input("Pressione qualquer tecla para continuar...")
    else:
        print("Opção inválida!")
        time.sleep(1)
        menu()