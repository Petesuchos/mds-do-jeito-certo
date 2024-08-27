import sqlite3
import json

# Passo 1: Criar a conexão com o banco de dados SQLite3
con = sqlite3.connect('vetdb.sqlite')
cur = con.cursor()

# Passo 2: Criar a tabela no SQLite3
cur.execute('''
    CREATE TABLE IF NOT EXISTS ANIMAIS (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        especie TEXT,
        raca TEXT,
        idade INTEGER,
        peso REAL,
        sexo TEXT,
        nome_dono TEXT,
        telefone_dono TEXT,
        data_ultima_consulta TEXT
    )
''')

# Passo 3: Ler o arquivo JSON
with open('dados_gatos.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

# Passo 4: Inserir os dados no banco de dados
for gato in dados:
    cur.execute('''
        INSERT INTO ANIMAIS (ID, NOME, ESPECIE, RACA, IDADE, PESO, SEXO, NOME_DONO, TELEFONE_DONO, DATA_ULTIMA_CONSULTA)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        gato['id'], gato['nome'], gato['especie'], gato['raca'],
        gato['idade'], gato['peso'], gato['sexo'], gato['nome_dono'],
        gato['telefone_dono'], gato['data_ultima_consulta']
    ))

# Passo 5: Salvar (commit) as mudanças e fechar a conexão
con.commit()
con.close()

print("Dados inseridos com sucesso no banco de dados SQLite3.")
