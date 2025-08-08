FROM python:3.11-slim

# Installer SQLite
RUN apt-get update && apt-get install -y sqlite3 && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000
CMD ["python", "app.py"]