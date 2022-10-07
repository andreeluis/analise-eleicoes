from genericpath import exists
import _utils.clearConsole as clearConsole
import time

def LerCSV():
    clearConsole.Clear()
    print("Selecione o caminho para ler o arquivo de dados (.csv)")
    print("-*-"*10)
    print("1 - Caminho padrão")
    print("2 - Caminho personalizado")
    print("\n\t0 - Sair\n")

    # Caminho padrão
    caminho = "votacaoMG.csv"

    opcao = int(input("Digite a opção desejada: "))
    if opcao == 0:
        exit()
    elif opcao == 1:
        return caminho
    elif opcao == 2:
        caminho = input("Digite o caminho do arquivo: ")
        if exists(caminho):
            return caminho
        else:
            print("Caminho inválido!")
            time.sleep(1)
            LeituraCSV()
    else:
        print("Opção inválida!")
        time.sleep(1)
        LeituraCSV()

def EscreverCSV():
    clearConsole.Clear()
    print("Selecione o caminho de escrita do arquivo de dados (.csv)")
    print("-*-"*10)
    print("1 - Caminho padrão")
    print("2 - Caminho personalizado")
    print("\n\t0 - Sair\n")

    # Caminho padrão
    caminho = "resultadoConsulta.csv"

    opcao = int(input("Digite a opção desejada: "))
    if opcao == 0:
        exit()
    elif opcao == 1:
        return str(caminho)
    elif opcao == 2:
        caminho = input("Digite o caminho do arquivo: ")
        if exists(caminho):
            if (input("Arquivo já existe, deseja sobrescrever? (s/n)") == "s"):
                return str(caminho)
            else:
                EscreverCSV()
            return str(caminho)
        else:
            open(caminho, "x").close()
            if exists(caminho):
                return str(caminho)
            else:
                print("Caminho inválido!")
                time.sleep(1)
                EscreverCSV()
    else:
        print("Opção inválida!")
        time.sleep(1)
        EscreverCSV()