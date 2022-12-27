# Dockerfile - NGINX

# Pull imagem base
FROM nginx:1.21-alpine

# Cria diretório de trabalho (container nginx)
RUN mkdir /projeto

# Remove arquivo conf deafut
RUN rm /etc/nginx/conf.d/default.conf

# Copia novo arquivo conf
COPY nginx.conf /etc/nginx/conf.d/

# Define diretório de trabalho após inicialização (container nginx)
WORKDIR /projeto
