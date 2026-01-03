FROM python:3.10-slim

# -------------------------
# Python runtime settings
# -------------------------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 🔑 CRITICAL: Fix Django import path
ENV PYTHONPATH=/app/lexbrief

# -------------------------
# System dependencies
# -------------------------
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# -------------------------
# App setup
# -------------------------
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy project source
COPY . .

# Collect static files (safe no-op in dev)
RUN python lexbrief/manage.py collectstatic --noinput || true

# -------------------------
# Start server (Render-compatible)
# -------------------------

ENV DJANGO_SETTINGS_MODULE=lexbrief.settings

CMD gunicorn lexbrief.wsgi:application \
    --bind 0.0.0.0:${PORT:-10000} \
    --workers 2 \
    --timeout 120
