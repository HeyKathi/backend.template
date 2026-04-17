FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "FastAPI_TicTacToe_Game_REST_API_Development_Project.main:app", "--host", "0.0.0.0", "--port", "8000"]