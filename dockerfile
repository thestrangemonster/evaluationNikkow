FROM python:3.11-slim

WORKDIR /app

# Copier les requirements et installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY . .

# Exposer le port Flask
EXPOSE 5000

# Variables d'environnement pour Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Commande pour démarrer l'application (attention aux guillemets)
CMD ["python", "app.py"]