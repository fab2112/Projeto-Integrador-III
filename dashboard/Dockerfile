# Dockerfile - Dashboard

# Pull imagem base
FROM python:3.10-slim

# Define diretório de trabalho (container python)
WORKDIR /dashboard

EXPOSE 8050

# Copia tudo para diretório projeto (container python)
COPY . /dashboard

# Instalação dependências
RUN pip install -r requirements.txt
RUN apt-get update && apt-get -y install libpq-dev gcc && pip install psycopg2

# Run in background docker run --name dashboard -d -p 80:80  dashboard:latest
CMD ["python3", "dashboard_001"]




