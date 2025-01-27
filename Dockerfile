# Usa una imagen base con RDKit preinstalado
FROM rdkit/rdkit:latest

# Instala Python y Streamlit
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install --no-cache-dir streamlit pandas requests

# Copia el código de la app al contenedor
WORKDIR /app
COPY . /app

# Expone el puerto para Streamlit
EXPOSE 8501

# Comando para ejecutar la aplicación
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
