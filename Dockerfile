FROM python:3.8-slim

# Instala dependencias del sistema operativo
RUN apt-get update && apt-get install -y \
    libxrender1 libsm6 libxext6 \
    python3-dev python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Instala RDKit y dependencias de Python
RUN pip install --no-cache-dir rdkit-pypi streamlit pandas requests

# Copia los archivos de la aplicación
WORKDIR /app
COPY . /app

# Expone el puerto y ejecuta la aplicación
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
