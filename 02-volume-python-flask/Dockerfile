FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Cria diretório para o banco de dados
RUN mkdir -p /data

ENV DB_PATH=/data/app.db

EXPOSE 3000

CMD ["python", "app.py"]