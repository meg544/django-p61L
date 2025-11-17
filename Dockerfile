# Imagen base
FROM python:3.11-slim

# Instalar dependencias del sistema para WeasyPrint
RUN apt-get update && apt-get install -y \
    build-essential \
    libpango-1.0-0 \
    libcairo2 \
    pango1.0-tools \
    libgdk-pixbuf-2.0-0 \
    libffi-dev \
    libfreetype6 \
    libharfbuzz0b \
    libfribidi0 \
    libxml2 \
    libjpeg62-turbo \
    fonts-dejavu-core \
    wget \
    && apt-get clean

# Set workdir
WORKDIR /app

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .
# Ejecutar collectstatic durante build
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# ---- AGREGAR ESTO ----
# Ejecutar collectstatic, migrate y levantar gunicorn
CMD ["sh", "-c", "python manage.py migrate && gunicorn mysite.wsgi --bind 0.0.0.0:8000"]
