import _utils.definirCaminhos as definirCaminhos
import csv

def EscreverDados(rows):
    with open(str(definirCaminhos.EscreverCSV()), 'w') as csvfile:
        for row in rows:
            csv.writer(csvfile, delimiter=',').writerow([row])
