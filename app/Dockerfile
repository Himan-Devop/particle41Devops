# Use lightweight Python base
FROM python:3.11-slim

# 1. Best practice: Prevent Python from writing .pyc files and keep logs flowing
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create non-root user
RUN useradd -m appuser
WORKDIR /home/appuser

# Install dependencies
COPY --chown=appuser:appuser requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code with correct ownership
COPY --chown=appuser:appuser app.py .

# Switch to non-root
USER appuser

# Expose port (Documentation only)
EXPOSE 8080

# Run app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]