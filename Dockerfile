FROM python:3.11-slim

# Instalar dependencias necesarias para WeasyPrint
RUN apt-get update && apt-get install -y \
    build-essential \
    libpango-1.0-0 \
    libcairo2 \
    libffi-dev \
    libgdk-pixbuf-2.0-0 \
    libxml2 \
    libxslt1.1 \
    libjpeg62-turbo \
    libpng-dev \
    && apt-get clean

# Crear ambiente virtual
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copiar aplicación
WORKDIR /app
COPY . /app

# Instalar requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Arrancar la aplicación
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:$PORT"]
