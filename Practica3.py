import pandas as pd
import numpy as np
from scipy import stats

# Cargar el archivo CSV con datos limpios
ruta_archivo_limpios = 'C:/Users/Lenovo e570/Desktop/Semestres/Septimo Semestre/Mineria de datos/athlete_events-copia.csv'  # Reemplaza con la ruta correcta
df = pd.read_csv(ruta_archivo_limpios)

# Medallero por edición
medallero_por_edicion = df[df['Medal'].notnull()].groupby(['Year', 'Medal'])['ID'].count().unstack(fill_value=0)

# Media de edad por país
media_por_pais = df.groupby('NOC')['Age'].mean()

# Rango de edad de todos los competidores de cada país
rango_edad_por_pais = df.groupby('NOC')['Age'].apply(lambda x: np.ptp(x))

# Moda de la edad por país
moda_por_pais = df.groupby('NOC')['Age'].apply(lambda x: stats.mode(x)[0][0])

# Estadísticas descriptivas generales
estadisticas_generales = df.describe()

# Guardar resultados en un archivo CSV
resultados = pd.concat([medallero_por_edicion, media_por_pais, rango_edad_por_pais, moda_por_pais, estadisticas_generales], axis=1)
resultados.to_csv('resultados.csv', index=True)

# Imprimir resultados
pd.set_option('display.max_columns', None)  # Para mostrar todas las columnas
print("Resultados guardados en 'resultados.csv'")

print("Medallero por edición:")
print(medallero_por_edicion)

print("\nMedia de edad por país:")
print(media_por_pais)

print("\nRango de edad de todos los competidores de cada país:")
print(rango_edad_por_pais)

print("\nModa de la edad por país:")
print(moda_por_pais)

print("\nEstadísticas descriptivas generales:")
print(estadisticas_generales)

