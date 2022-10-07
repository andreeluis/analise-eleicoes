import csv
import sqlite3

def popularBanco(caminho):
    with open(caminho, 'r', encoding='latin1', errors='replace') as csvfile:
        csv_file_reader = csv.reader(csvfile, delimiter=';')
        next(csv_file_reader, None)

        DtGeracao = ''
        HhGeracao = ''
        AnoEleicao = ''
        CdTipoEleicao = ''
        NmTipoEleicao = ''
        NrTurno = ''
        CdEleicao = ''
        DsEleicao = ''
        DtEleicao = ''
        TpAbrangencia = ''
        SgUf = ''
        SgUe = ''
        NmUe = ''
        CdMunicipio = ''
        NmMunicipio = ''
        NrZona = ''
        NrSecao = ''
        CdCargo = ''
        DsCargo = ''
        NrVotavel = ''
        NmVotavel = ''
        QtVotos = ''
        NrLocalVotacao = ''
        SqCandidato = ''

        connection=sqlite3.connect('votacaoMG.db')
        curosr=connection.cursor()

        curosr.execute('''
            CREATE TABLE if not Exists Votos(
                DT_GERACAO TEXT,
                HH_GERACAO TEXT,
                ANO_ELEICAO TEXT,
                CD_TIPO_ELEICAO INTEGER,
                NM_TIPO_ELEICAO TEXT,
                NR_TURNO TINYINT,
                CD_ELEICAO INTEGER,
                DS_ELEICAO TEXT,
                DT_ELEICAO CHARACTER(10),
                TP_ABRANGENCIA CHARACTER(5),
                SG_UF CHARACTER(2),
                SG_UE CHARACTER(5),
                NM_UE CHARACTER(20),
                CD_MUNICIPIO INTEGER,
                NM_MUNICIPIO CHARACTER(40),
                NR_ZONA INTEGER,
                NR_SECAO INTEGER,
                CD_CARGO INTEGER,
                DS_CARGO TEXT,
                NR_VOTAVEL INTEGER,
                NM_VOTAVEL TEXT,
                QT_VOTOS INTEGER,
                NR_LOCAL_VOTACAO INTEGER,
                SQ_CANDIDATO INTEGER
            )'''
        )

        for row in csv_file_reader:
            DtGeracao = row[0]
            HhGeracao = row[1]
            AnoEleicao = row[2]
            CdTipoEleicao = row[3]
            NmTipoEleicao = row[4]
            NrTurno = row[5]
            CdEleicao = row[6]
            DsEleicao = row[7]
            DtEleicao = row[8]
            TpAbrangencia = row[9]
            SgUf = row[10]
            SgUe = row[11]
            NmUe = row[12]
            CdMunicipio = row[13]
            NmMunicipio = row[14]
            NrZona = row[15]
            NrSecao = row[16]
            CdCargo = row[17]
            DsCargo = row[18]
            NrVotavel = row[19]
            NmVotavel = row[20]
            QtVotos = row[21]
            NrLocalVotacao = row[22]
            SqCandidato = row[23]

            curosr.execute(f"INSERT INTO Votos VALUES ('{DtGeracao}', '{HhGeracao}', '{AnoEleicao}', '{CdTipoEleicao}', '{NmTipoEleicao}', '{NrTurno}', '{CdEleicao}', '{DsEleicao}', '{DtEleicao}', '{TpAbrangencia}', '{SgUf}', '{SgUe}', '{NmUe}', '{CdMunicipio}', '{NmMunicipio}', '{NrZona}', '{NrSecao}', '{CdCargo}', '{DsCargo}', '{NrVotavel}', '{NmVotavel}', '{QtVotos}', '{NrLocalVotacao}', '{SqCandidato}')")
        connection.commit()
        connection.close()