FROM python:3.10-slim

WORKDIR /app

COPY main.py .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "main.py"]
