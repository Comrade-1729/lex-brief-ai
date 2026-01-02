FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# System dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Django collectstatic (safe no-op)
RUN python lexbrief/manage.py collectstatic --noinput || true

EXPOSE 8000

CMD ["gunicorn", "lexbrief.lexbrief.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2", "--timeout", "120"]
