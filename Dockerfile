# Dockerfile
FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Avoid buffering stdout
ENV PYTHONUNBUFFERED=1

# Copy and install requirements first for caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app and model
COPY . /app

# Expose port
EXPOSE 8000

# Default command
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers"]
