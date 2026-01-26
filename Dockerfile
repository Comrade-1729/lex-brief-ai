FROM python:3.11-slim

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

# before migrate
ENV DJANGO_SETTINGS_MODULE=lexbrief.settings

# Prepare Django & Collect static files (safe no-op in dev)
RUN python lexbrief/manage.py migrate --noinput
RUN python lexbrief/manage.py collectstatic --noinput || true

# -------------------------
# Start server (Render-compatible)
# -------------------------

ENV DJANGO_SETTINGS_MODULE=lexbrief.settings

CMD gunicorn lexbrief.wsgi:application \
    --bind 0.0.0.0:${PORT:-10000} \
    --workers 1 \
    --timeout 120
