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

# Crear directorio de app
WORKDIR /app

# Copiar archivos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exponer puerto
EXPOSE 8000



