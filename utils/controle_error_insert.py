
## Forma correcta de pegar insercao evitando qualquer erro seja levado ao banco de dados 

import os
import duckdb

con = duckdb.connect()

caminho = "C:\\Users\\Jeremias\\Desktop\\Outros Projectos\\Base de Dados\\BIG DATA SALES\\2019-Oct.csv"
nome_ficheiro = os.path.basename(caminho)

try:
    con.execute("BEGIN")

    con.execute("""
        CREATE OR REPLACE TEMP TABLE vendas_brutos AS
        SELECT * FROM read_csv_auto(?)
    """, (caminho,))

    # aqui entraria o processamento / insert na tabela final

    con.execute("""
        INSERT INTO ficheiro_processados (nome_ficheiro)
        VALUES (?)
    """, (nome_ficheiro,))

    con.execute("COMMIT")

except Exception as e:
    con.execute("ROLLBACK")
    print(f"Erro ao processar ficheiro {nome_ficheiro}: {e}")
