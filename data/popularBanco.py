import csv
import sqlite3

def popularBanco(caminho):
    with open(caminho, 'r', encoding='latin1', errors='replace') as csvfile:
        csv_file_reader = csv.reader(csvfile, delimiter=';')
        next(csv_file_reader, None)

        connection=sqlite3.connect('votacao.db')
        curosr=connection.cursor()

        curosr.execute('''
            CREATE TABLE if not Exists Votos(
                DT_GERACAO TEXT,
                HH_GERACAO TEXT,
                ANO_ELEICAO TEXT,
                CD_TIPO_ELEICAO INTEGER(1),
                NM_TIPO_ELEICAO TEXT,
                CD_PLEITO INTEGER,
                DT_PLEITO TEXT,
                NR_TURNO INTEGER(1),
                CD_ELEICAO INTEGER,
                DS_ELEICAO TEXT,
                SG_UF TEXT,
                CD_MUNICIPIO INTEGER,
                NM_MUNICIPIO TEXT,
                NR_ZONA INTEGER,
                NR_SECAO INTEGER,
                NR_LOCAL_VOTACAO INTEGER,
                CD_CARGO_PERGUNTA INTEGER,
                DS_CARGO_PERGUNTA TEXT,
                NR_PARTIDO INTEGER,
                SG_PARTIDO TEXT,
                NM_PARTIDO TEXT,
                DT_BU_RECEBIDO TEXT,
                QT_APTOS INTEGER,
                QT_COMPARECIMENTO INTEGER,
                QT_ABSTENCOES INTEGER,
                CD_TIPO_URNA INTEGER,
                DS_TIPO_URNA TEXT,
                CD_TIPO_VOTAVEL INTEGER,
                DS_TIPO_VOTAVEL TEXT,
                NR_VOTAVEL INTEGER,
                NM_VOTAVEL TEXT,
                QT_VOTOS INTEGER,
                NR_URNA_EFETIVADA INTEGER,
                CD_CARGA_1_URNA_EFETIVADA INTEGER,
                CD_CARGA_2_URNA_EFETIVADA INTEGER,
                CD_FLASHCARD_URNA_EFETIVADA INTEGER,
                DT_CARGA_URNA_EFETIVADA TEXT,
                DS_CARGO_PERGUNTA_SECAO TEXT,
                DS_AGREGADAS TEXT,
                DT_ABERTURA TEXT,
                DT_ENCERRAMENTO TEXT,
                QT_ELEITORES_BIOMETRIA_NH INTEGER,
                DT_EMISSAO_BU TEXT,
                NR_JUNTA_APURADORA INTEGER,
                NR_TURMA_APURADORA INTEGER
            )'''
        )

        for row in csv_file_reader:
            dtGeracao = row[0]
            hhGeracao = row[1]
            anoEleicao = row[2]
            cdTipoEleicao = row[3]
            nmTipoEleicao = row[4]
            cdPleito = row[5]
            dtPleito = row[6]
            nrTurno = row[7]
            cdEleicao = row[8]
            dsEleicao = row[9]
            sgUf = row[10]
            cdMunicipio = row[11]
            nmMunicipio = row[12]
            nrZona = row[13]
            nrSecao = row[14]
            nrLocalVotacao = row[15]
            cdCargoPergunta = row[16]
            dsCargoPergunta = row[17]
            nrPartido = row[18]
            sgPartido = row[19]
            nmPartido = row[20]
            dtBuRecebido = row[21]
            qtAptos = row[22]
            qtComparecimento = row[23]
            qtAbstencoes = row[24]
            cdTipoUrna = row[25]
            dsTipoUrna = row[26]
            cdTipoVotavel = row[27]
            dsTipoVotavel = row[28]
            nrVotavel = row[29]
            nmVotavel = row[30]
            qtVotos = row[31]
            nrUrnaEfetivada = row[32]
            cdCarga1UrnaEfetivada = row[33]
            cdCarga2UrnaEfetivada = row[34]
            cdFlashcardUrnaEfetivada = row[35]
            dtCargaUrnaEfetivada = row[36]
            dsCargoPerguntaSecao = row[37]
            dsAgregadas = row[38]
            dtAbertura = row[39]
            dtEncerramento = row[40]
            qtEleitoresBiometriaNh = row[41]
            dtEmissaoBu = row[42]
            nrJuntaApuradora = row[43]
            nrTurmaApuradora = row[44]

            curosr.execute(f'''INSERT INTO Votos VALUES(
                    "{dtGeracao}",
                    "{hhGeracao}",
                    "{anoEleicao}",
                    "{cdTipoEleicao}",
                    "{nmTipoEleicao}",
                    "{cdPleito}",
                    "{dtPleito}",
                    "{nrTurno}",
                    "{cdEleicao}",
                    "{dsEleicao}",
                    "{sgUf}",
                    "{cdMunicipio}",
                    "{nmMunicipio}",
                    "{nrZona}",
                    "{nrSecao}",
                    "{nrLocalVotacao}",
                    "{cdCargoPergunta}",
                    "{dsCargoPergunta}",
                    "{nrPartido}",
                    "{sgPartido}",
                    "{nmPartido}",
                    "{dtBuRecebido}",
                    "{qtAptos}",
                    "{qtComparecimento}",
                    "{qtAbstencoes}",
                    "{cdTipoUrna}",
                    "{dsTipoUrna}",
                    "{cdTipoVotavel}",
                    "{dsTipoVotavel}",
                    "{nrVotavel}",
                    "{nmVotavel}",
                    "{qtVotos}",
                    "{nrUrnaEfetivada}",
                    "{cdCarga1UrnaEfetivada}",
                    "{cdCarga2UrnaEfetivada}",
                    "{cdFlashcardUrnaEfetivada}",
                    "{dtCargaUrnaEfetivada}",
                    "{dsCargoPerguntaSecao}",
                    "{dsAgregadas}",
                    "{dtAbertura}",
                    "{dtEncerramento}",
                    "{qtEleitoresBiometriaNh}",
                    "{dtEmissaoBu}",
                    "{nrJuntaApuradora}",
                    "{nrTurmaApuradora}"
                )''')
        connection.commit()
        connection.close()