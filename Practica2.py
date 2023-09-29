import pandas as pd

# Especifica la ruta completa al archivo CSV
ruta_archivo = 'C:/Users/Lenovo e570/Desktop/Semestres/Septimo Semestre/Mineria de datos/athlete_events.csv'

# Cargar el archivo CSV
df = pd.read_csv('C:/Users/Lenovo e570/Desktop/Semestres/Septimo Semestre/Mineria de datos/athlete_events.csv')

# Eliminar registros con valores NA o nulos
df_cleaned = df.dropna()

# Imprimir los registros limpios
print("Registros limpios:")
print(df_cleaned)

# Guardar una copia del archivo CSV con los datos limpios
ruta_archivo_limpios = 'C:/Users/Lenovo e570/Desktop/Semestres/Septimo Semestre/Mineria de datos/athlete_events-copia.csv'
df_cleaned.to_csv(ruta_archivo_limpios, index=False)

print("Archivo CSV con datos limpios guardado como 'tu_archivo_limpios.csv'")
