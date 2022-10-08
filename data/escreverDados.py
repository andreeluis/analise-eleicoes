from dataclasses import replace
import _utils.definirCaminhos as definirCaminhos
import csv

def EscreverDados(nomeColunas, dados):
    with open(str(definirCaminhos.EscreverCSV()), 'w') as csvfile:
        csv.writer(csvfile, delimiter=',', escapechar = ',', quoting = csv.QUOTE_NONE).writerow(nomeColunas)
        for row in dados:
            csv.writer(csvfile, delimiter=',', escapechar = ',', quoting = csv.QUOTE_NONE).writerow(row)
