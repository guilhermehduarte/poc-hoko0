# Use uma imagem oficial do Python como base
FROM python:3.8-slim-buster

# Define o diretório de trabalho no container
WORKDIR /app

# Copia os arquivos necessários para o container
COPY requirements.txt ./
COPY server.py ./

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Instala o Gunicorn
RUN pip install gunicorn

# Expõe a porta do servidor Flask
EXPOSE 10000

# Comando para iniciar o servidor Flask com Gunicorn
CMD [ "gunicorn", "-b", "0.0.0.0:10000", "server:app" ]
