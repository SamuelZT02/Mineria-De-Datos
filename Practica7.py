import pandas as pd
import matplotlib.pyplot as plt

# Carga el archivo CSV en un DataFrame
df = pd.read_csv('C:/Users/Lenovo e570/Desktop/Semestres/Septimo Semestre/Mineria de datos/athlete_events-copia.csv')

# Selecciona el país que deseas analizar
pais_seleccionado = 'Australia'  # Cambia 'Algeria' al país que desees analizar

# Filtra los datos para el país seleccionado
datos_pais = df[df['Team'] == pais_seleccionado]

# Agrupa los datos por año y cuenta el número de entradas por año
clasificacion_por_anio = datos_pais['Year'].value_counts().sort_index()

# Crea un gráfico de barras para mostrar la clasificación por año
plt.figure(figsize=(10, 6))
clasificacion_por_anio.plot(kind='bar', color='skyblue')
plt.title(f'Clasificación por Año para {pais_seleccionado}')
plt.xlabel('Año')
plt.ylabel('Número de Participantes')
plt.xticks(rotation=45)
plt.show()









