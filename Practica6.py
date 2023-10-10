import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Carga los datos desde el archivo CSV
ruta_archivo_limpios = 'C:/Users/Lenovo e570/Desktop/Semestres/Septimo Semestre/Mineria de datos/athlete_events-copia.csv'
df = pd.read_csv(ruta_archivo_limpios)

df = df.dropna(subset=['Height', 'Weight'])

altura = df['Height'].values.reshape(-1, 1)
peso = df['Weight'].values

modelo = LinearRegression()
modelo.fit(altura, peso)

predicciones_peso = modelo.predict(altura)

plt.scatter(altura, peso, color='blue', label='Datos reales')
plt.plot(altura, predicciones_peso, color='red', linewidth=2, label='Línea de Regresión')
plt.title('Regresión Lineal: Altura vs Peso')
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.legend()
plt.grid(True)
plt.show()