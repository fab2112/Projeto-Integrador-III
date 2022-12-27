# Dockerfile - python

# Pull imagem base
FROM python:3.10-slim

# Variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Define diretório de trabalho (container python)
WORKDIR /projeto

# Copia tudo para diretório projeto (container python)
COPY . /projeto

# Instalação dependências
RUN apt-get update && apt-get -y install libpq-dev gcc && pip install psycopg2
RUN pip install pipenv && pipenv install --system
#COPY requirements.txt /projeto/
#RUN pip install -r requirements.txt





