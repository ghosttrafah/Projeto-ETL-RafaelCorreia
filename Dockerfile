# Comando para usar uma imagem de base oficial do Python no projeo
FROM python:3.9-slim

# Comando que vai definir o diretório de trabalho no contêiner do docker
WORKDIR /app

# Comando que vai copiar os aquivos de requisitos para o contêiner (que será preenchido no txt de requerimentos)
COPY requirements.txt .

# Comando que vai instalar as depend~encias
RUN pip install --no-cache-dir -r requirements.txt

# Comando que copiara o arquivo do kaggle.json para o diretório /root/.kaggle
RUN mkdir -p /root/.kaggle
COPY kaggle.json /root/.kaggle/

# Copia todo o conteúdo da aplicação para o contêiner
COPY . .

# Comando que vai rodar o script principal
CMD ["python", "main.py"]

#comando para abrir um shell interativo, pois obtive erro na construção da imagem e esse comando ajuda a entender
#CMD ["sh"]