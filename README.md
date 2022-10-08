# Analise Eleições

## Como usar?
Você precisará baixar os dados no [site do TSE](https://dadosabertos.tse.jus.br/dataset/resultados-2022-boletim-de-urna), onde se encontra os arquivos .csv para download.

![site_tse](https://user-images.githubusercontent.com/52361683/194722200-7d3a7ca0-717d-4630-a80e-b1b0a2207efe.png)

Clicando em "Explorar", e logo após clicando em "Ir para recurso", o download dos arquivos começará.

---

Após o download do arquivo que vem em ZIP, será preciso extrair o arquivo .csv que está dentro. Recomendo colocar na mesma pasta do projeto, com o nome "votacao.csv", pois o código já está configurado para pegar esse arquivo por padrão (é possível deixar em outro caminho, basta informar ao programa).

Agora apenas precisa executar o arquivo "main.py" e seguir o passo a passo.

---

## Funcionamento do código
### 1 - Inserir dados
Recebe e lê um .csv (arquivo completo, baixado no site do TSE) e copia esse arquivo para um banco de dados SQLite3.

### 2 - Analisar dados
Recebe do usuário o número da **zona eleitoral** e o **número da seção**.
Logo após faz-se a consulta no banco de dados retornando um arquivo .csv com os dados filtrados.

---

A grande vantagem desse código é o uso de um banco de dados, que com simples comandos SQL consegue-se fazer vários filtros em disco, já que o arquivo original (.csv do TSE) pode ter até gigabytes de tamanho. 
