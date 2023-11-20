import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Carga los datos desde el archivo CSV
ruta_archivo_limpios = 'C:/Users/Lenovo e570/Desktop/Semestres/Septimo Semestre/Mineria de datos/athlete_events-copia.csv'
df = pd.read_csv(ruta_archivo_limpios)

# Muestra los primeros registros del DataFrame para identificar el nombre de la columna
print(df.head())

# Reemplaza 'nombre_de_columna' con el nombre real de la columna que contiene el texto
nombre_columna_texto = 'Sport'  # Puedes cambiar esto a 'Event' si prefieres esa columna
texto_para_wordcloud = ' '.join(df[nombre_columna_texto].dropna())

# Crea la nube de palabras
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(texto_para_wordcloud)

# Muestra la nube de palabras utilizando matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
