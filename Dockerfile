# Base Image
FROM python:3.12-slim

# Working Directory
WORKDIR /app

# Copy dependency
COPY requirements.txt .

# Install dependency
RUN pip install --no-cache-dir -r requirements.txt

# Copy semua source code
COPY . .

# Expose Port
EXPOSE 5000

# Menjalankan aplikasi
CMD ["python", "app.py"]