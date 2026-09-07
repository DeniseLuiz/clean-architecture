# Usando Python 3.11 slim (mais recente, leve e estável)
FROM python:3.11-slim

# Evita que o Python grave arquivos .pyc e garante saída imediata dos logs no terminal
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Define o diretório de trabalho dentro do container
WORKDIR /src

# 1. Copia APENAS o requirements.txt primeiro (Aproveita o Cache do Docker)
COPY requirements.txt /src/requirements.txt

# 2. Atualiza o pip e instala as dependências sem armazenar cache desnecessário
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# 3. Copia o restante do código da aplicação
COPY ./src /src

# Expõe a porta do FastAPI
EXPOSE 8000

# Comando padrão
CMD ["uvicorn", "infra.api.main:app", "--host", "0.0.0.0", "--port", "8800"]