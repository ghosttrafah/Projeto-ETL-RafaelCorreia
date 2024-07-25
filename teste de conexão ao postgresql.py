from sqlalchemy import create_engine
from urllib.parse import quote_plus
import pandas as pd

# Configurações de conexão
username = 'postgres'
db_password = quote_plus('IDshell18@')
host = 'localhost'
port = '5432'
database = 'ETL DB Rafa'

engine = create_engine(f'postgresql+psycopg2://{username}:{db_password}@{host}:{port}/{database}')

try:
    # Exemplo de criação de DataFrame e inserção no PostgreSQL
    data = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data)
    df.to_sql('Jira_data', engine, if_exists='replace', index=False)
    print("Tabela criada com sucesso!")
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
