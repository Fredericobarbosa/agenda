FROM python:3.11-slim-bullseye

# Atualiza pacotes do sistema e instala dependências do sistema necessárias para mysqlclient funcionar
RUN apt-get update && \
    apt-get install -y gcc default-libmysqlclient-dev pkg-config && \
    rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos da aplicação
COPY . /app

# Instala dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta do Flask
EXPOSE 5000

# Comando padrão ao iniciar o container
CMD ["python", "run.py"]