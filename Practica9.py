import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Carga el archivo CSV en un DataFrame
df = pd.read_csv('C:/Users/Lenovo e570/Desktop/Semestres/Septimo Semestre/Mineria de datos/athlete_events-copia.csv')

# Selección de variables predictoras y objetivo
X = df[['Age', 'Height', 'Weight', 'Year']]
y = df['Medal']

# División de los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenamiento del modelo de clasificación (por ejemplo, Random Forest)
modelo = RandomForestClassifier()
modelo.fit(X_train, y_train)

# Evaluación del modelo
y_pred = modelo.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {accuracy}")

# Visualización de la matriz de confusión
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Valores Pronosticados')
plt.ylabel('Valores Reales')
plt.title('Matriz de Confusión')
plt.show()

# Visualización de la distribución de categorías pronosticadas
pred_counts = pd.Series(y_pred).value_counts()
plt.figure(figsize=(8, 6))
pred_counts.plot(kind='bar', color='skyblue')
plt.xlabel('Categoría Pronosticada')
plt.ylabel('Cantidad')
plt.title('Distribución de Categorías Pronosticadas')
plt.xticks(rotation=45)
plt.show()

# Realización de pronósticos en nuevos datos
nuevos_datos = pd.DataFrame({'Age': [30], 'Height': [180], 'Weight': [75], 'Year': [2025]})
pronostico = modelo.predict(nuevos_datos)
print(f"Pronóstico: {pronostico}")




