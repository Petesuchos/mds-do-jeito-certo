import sqlite3
import json
import random
from datetime import datetime, timedelta

def gerar_dados(caminho_arquivo_nome_gato, caminho_arquivo_raca_gato, caminho_arquivo_nome, caminho_arquivo_sobrenome, num_registros=1000):
    # Ler os dados dos arquivos de texto
    with open(caminho_arquivo_nome_gato, 'r', encoding='utf-8') as f:
        nomes_gatos = f.read().splitlines()
    
    with open(caminho_arquivo_raca_gato, 'r', encoding='utf-8') as f:
        racas_gatos = f.read().splitlines()
    
    with open(caminho_arquivo_nome, 'r', encoding='utf-8') as f:
        nomes = f.read().splitlines()
        
    with open(caminho_arquivo_sobrenome, 'r', encoding='utf-8') as f:
        sobrenomes = f.read().splitlines()
    
    registros = []
    
    for i in range(1, num_registros + 1):
        # Gerar dados aleatórios
        nome_gato = random.choice(nomes_gatos)
        raca_gato = random.choice(racas_gatos)
        idade_gato = int(random.triangular(1, 15, 4))
        peso_gato = round(random.gauss(5.0, 2.5), 2)
        sexo_gato = random.choice(['M', 'F'])
        
        # Compor nome de dono com nome e sobrenome
        nome_dono = f"{random.choice(nomes)} {random.choice(sobrenomes)}"
        
        telefone_dono = f"({random.randint(10, 99)}) {random.randint(1000, 9999)}-{random.randint(1000, 9999)}"
        data_ultima_consulta = (datetime.now() - timedelta(days=random.randint(0, 180))).strftime('%Y-%m-%d')
        
        # Criar registro
        registro = {
            "id": i,
            "nome": nome_gato,
            "especie": "Gato",
            "raca": raca_gato,
            "idade": idade_gato,
            "peso": peso_gato,
            "sexo": sexo_gato,
            "nome_dono": nome_dono,
            "telefone_dono": telefone_dono,
            "data_ultima_consulta": data_ultima_consulta
        }
        
        registros.append(registro)
    
    # Salvar os registros no arquivo JSON com codificação UTF-8
    with open('dados_gatos.json', 'w', encoding='utf-8') as f:
        json.dump(registros, f, indent=4, ensure_ascii=False)
    
    return 'dados_gatos.json'

# Exemplo de uso
caminho_arquivo_nome_gato = 'nomes_gatos.txt'
caminho_arquivo_raca_gato = 'racas_gatos.txt'
caminho_arquivo_nome = 'nomes_comuns_brasil.txt'
caminho_arquivo_sobrenome = 'sobrenomes_comuns_brasil.txt'

# Gerar o arquivo JSON com os dados
gerar_dados(caminho_arquivo_nome_gato, caminho_arquivo_raca_gato, caminho_arquivo_nome, caminho_arquivo_sobrenome)
