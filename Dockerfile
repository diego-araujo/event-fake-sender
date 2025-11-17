# Usar imagem base do Python
FROM python:3.11-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar e instalar as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar os arquivos da aplicação (incluindo a pasta json_files)
COPY app/ /app/

# Expor a porta 80 para o Gunicorn
EXPOSE 80

# Comando para iniciar a aplicação com Gunicorn
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:80", "app:app"]