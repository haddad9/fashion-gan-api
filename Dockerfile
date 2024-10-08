FROM python:3.9-slim

WORKDIR /app/src

# Copy reqs
COPY requirements.txt /app/src

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY ./src /app/src

EXPOSE 8080

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]