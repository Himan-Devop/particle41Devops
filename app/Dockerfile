# Stage 1: Build dependencies
FROM python:3.11-alpine AS builder

# Prevent .pyc files and keep logs flowing
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install build tools (only for compiling dependencies)
RUN apk add --no-cache gcc musl-dev libffi-dev

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Runtime image
FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create non-root user
RUN adduser -D appuser
WORKDIR /home/appuser

# Copy installed packages from builder
COPY --from=builder /install /usr/local

# Copy app code
COPY --chown=appuser:appuser app.py .

USER appuser

EXPOSE 8080

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]