# 1. Basisimage
FROM python:3.11-slim

# 2. Arbeitsverzeichnis im Container
WORKDIR /app

# 3. Abhängigkeiten installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Projektcode kopieren (alles in /app)
COPY . .

# 5. Port freigeben
EXPOSE 8000

# 6. Uvicorn starten
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]