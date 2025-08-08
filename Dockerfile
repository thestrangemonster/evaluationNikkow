FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Créer le dossier instance s'il n'existe pas
RUN mkdir -p /app/instance

EXPOSE 5000
CMD ["python", "app.py"]