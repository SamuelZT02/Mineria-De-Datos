import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo CSV con datos limpios
ruta_archivo_limpios = 'C:/Users/Lenovo e570/Desktop/Semestres/Septimo Semestre/Mineria de datos/athlete_events-copia.csv'  # Reemplaza con la ruta correcta
df = pd.read_csv(ruta_archivo_limpios)

while True:
    print("Selecciona una opción:")
    print("1. Ver Medallero por edición")
    print("2. Ver Media de Edad por País")
    print("3. Ver Rango de Edad por País")
    print("4. Ver Moda de Edad por País")
    print("5. Ver Histograma de Edades")
    print("0. Salir")

    opcion = input("Ingresa el número de la opción que deseas (0-5): ")

    if opcion == "0":
        print("Saliendo del programa.")
        break
    elif opcion == "1":
        medallero_por_edicion = df[df['Medal'].notnull()].groupby(['Year', 'Medal'])['ID'].count().unstack(fill_value=0)
        medallero_por_edicion.plot(kind='bar', stacked=True)
        plt.title('Medallero por edición')
        plt.xlabel('Año')
        plt.ylabel('Cantidad de medallas')
        plt.show()
    elif opcion == "2":
        media_por_pais = df.groupby('NOC')['Age'].mean()
        media_por_pais.plot(kind='bar')
        plt.title('Media de Edad por País')
        plt.xlabel('País')
        plt.ylabel('Media de Edad')
        plt.show()
    elif opcion == "3":
        rango_edad_por_pais = df.groupby('NOC')['Age'].apply(lambda x: np.ptp(x))
        rango_edad_por_pais.plot(kind='bar')
        plt.title('Rango de Edad por País')
        plt.xlabel('País')
        plt.ylabel('Rango de Edad')
        plt.show()
    elif opcion == "4":
        moda_por_pais = df.groupby('NOC')['Age'].apply(lambda x: stats.mode(x)[0][0])
        moda_por_pais.plot(kind='bar')
        plt.title('Moda de Edad por País')
        plt.xlabel('País')
        plt.ylabel('Moda de Edad')
        plt.show()
    elif opcion == "5":
        df['Age'].plot(kind='hist', bins=20)
        plt.title('Histograma de Edades')
        plt.xlabel('Edad')
        plt.ylabel('Frecuencia')
        plt.show()
    else:
        print("Opción no válida. Por favor, ingresa un número válido del menú (0-5).")