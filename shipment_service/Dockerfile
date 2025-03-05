# Dockerfile (customer service)
FROM python:3.11

# Cài đặt dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy source code
COPY . .

# Chạy server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "shipment_service.wsgi:application"]
