import sqlite3
from _utils.definirCaminhos import EscreverCSV
import data.escreverDados as escreverDados
import _utils.clearConsole as clearConsole

def Menu():
    clearConsole.Clear()
    print("Insira as informações para a consulta no banco de dados: ")
    zona = str(input("Zona eleitoral: "))
    secao = str(input("Seção: "))
    
    return [zona, secao]

def LerDados():
    dados = Menu()
    zona = dados[0]
    secao = dados[1]

    query = '''
        SELECT DISTINCT
            NM_TIPO_ELEICAO,
            NR_TURNO,
            CD_ELEICAO,
            DT_ELEICAO,
            SG_UE,
            NM_UE,
            CD_MUNICIPIO,
            NM_MUNICIPIO,
            NR_ZONA,
            NR_SECAO,
            CD_CARGO,
            DS_CARGO,
            NR_VOTAVEL,
            NM_VOTAVEL,
            QT_VOTOS,
            NR_LOCAL_VOTACAO
        FROM
            Votos'''

    if zona == '' and secao == '':
        if(input("Gostaria de mostrar todos os dados? (s/n) ") == 's'):
            pass    
        else:
            LerDados()

        print("Mostrando dados de todas as zonas e de todas seções.")
    elif zona != '' and secao == '':
        print(f"Mostrando dados da(s) zona(s): {zona} e de todas as seções.")
        query += f'''\nWHERE NR_ZONA in ({zona})
            ORDER BY NR_ZONA, NR_SECAO'''
        
    elif secao != '' and zona == '':
        print(f"Mostrando dados de todas as zonas e da(a) seção(es): {secao}.")
        query += f'''\nWHERE NR_SECAO in ({secao})
            ORDER BY NR_ZONA, NR_SECAO'''
    else:   
        print(f"Mostrando dados da(s) zona(s): {zona} e da(a) seção(es): {secao}.")
        query += f'''WHERE
            NR_ZONA in ({zona})
            AND NR_SECAO in ({secao})
            ORDER BY NR_ZONA, NR_SECAO'''

    connection=sqlite3.connect('votacaoMG.db')
    curosr=connection.cursor()

    curosr.execute(query)
    rows = curosr.fetchall()

    escreverDados.EscreverDados(rows)

    

    