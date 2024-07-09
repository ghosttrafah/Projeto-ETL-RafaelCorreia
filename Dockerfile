# Comando para usar uma imagem de base oficial do Python no projeo
FROM python:3.9-slim

# Comando que vai definir o diretório de trabalho no contêiner do docker
WORKDIR /app

# Comando que vai copiar os aquivos de requisitos para o contêiner (que será preenchido no txt de requerimentos)
COPY requirements.txt .

# Comando que vai instalar as depend~encias
RUN pip install --no-cache-dir -r requirements.txt


# Copia todo o conteúdo da aplicação para o contêiner
COPY . .

# Comando que vai rodar o script principal
CMD ["python", "main.py"]
