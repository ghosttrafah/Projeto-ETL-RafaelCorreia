import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from urllib.parse import quote_plus 

#Esse código vai automatizar a criação de tabela no banco de dados

#declaração de Dados de conexão
db_user = 'postgres'
db_password = quote_plus('IDshell18@')
db_host = 'localhost'
db_port = '5432'
db_name = 'ETL DB Rafa'

#caminho do dataset CSV
csv_file_path = 'C:/Users/color/Documents/Projeto Rafa - ETL F1rst/Projeto-ETL-RafaelCorreia/data/GFG_FINAL.csv'

#Dado os erros de conexão adicionei o código de verificação
try:
    engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
    with engine.connect() as connection:
        print("Conexão com o banco de dados bem-sucedida!")
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")

#para fazer a leitura dos dados
df = pd.read_csv(csv_file_path)

#criação de conexão com o banco de dados
engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')



#informações da tabela a ser criada
table_name = 'jira_infos'

#converter o dataframe para uma tabela SQL
df.to_sql(table_name, engine, if_exists='replace', index=False)

print(f"Tabela '{table_name}' criada com sucesso no seu banco de dados '{db_name}'!")
