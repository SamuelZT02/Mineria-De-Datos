import requests
import os

# URL del archivo CSV en Google Storage
url = "https://storage.googleapis.com/kaggle-data-sets/1759/10512/bundle/archive.zip"

# Ruta donde guardar el archivo CSV descargado
csv_download_path = "C:/Users/Lenovo e570/Desktop/Semestres/Septimo Semestre/Mineria de datos/datos/olympic_data.csv"

# Descarga el archivo CSV
response = requests.get(url)
if response.status_code == 200:
    with open(csv_download_path, 'wb') as file:
        file.write(response.content)
    print(f"El archivo CSV se ha descargado en {csv_download_path}.")
else:
    print("Error al descargar el archivo. Código de estado:", response.status_code)
