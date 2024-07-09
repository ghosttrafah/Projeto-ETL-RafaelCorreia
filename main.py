import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Configurações de API do Kaggle
os.environ['KAGGLE_USERNAME'] = 'rafaelscorreia'
os.environ['KAGGLE_KEY'] = 'b3acdfe1376ee48b4f08ea1641292dd6'

# comandos para inicializar a api do kaggle
api = KaggleApi()
api.authenticate()

# comando para selecionar o dataset especifico, considerando a conexão de api realizada
dataset = 'cesaranasco/jira-dataset' #colocar o nome do dataset q escolher
destination_path = '/app/data' #local onde os dados serão salvos

# caso o diretório não existir esse comando o criará
os.makedirs(destination_path, exist_ok=True)

# Baixar o data set via api
api.dataset_download_files(dataset, path=destination_path, unzip=True)

print("Dados baixados com sucesso!")

