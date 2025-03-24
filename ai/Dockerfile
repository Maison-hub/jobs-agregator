FROM python:3.11

# Définir le dossier de travail
WORKDIR /app

# Installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Installer Ollama
RUN apt-get update && apt-get install -y \
    ollama-dependency1 \
    ollama-dependency2

COPY ./ollama /root/.ollama

# Copier le code FastAPI
COPY . /app

# Exposer le port de FastAPI
EXPOSE 5001

# Lancer l'application
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port 5001 & ollama --config /root/.ollama/config.yaml"]