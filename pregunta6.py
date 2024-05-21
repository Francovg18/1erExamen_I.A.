import csv
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

# Cargar datos
datos = []
ruta_archivo = "C:/Users/Alex Choque/Downloads/iris.csv"

with open(ruta_archivo, newline='') as csvfile:
    lector = csv.reader(csvfile)
    for fila in lector:
        datos.append(fila)
# Cargar los datos en un DataFrame
df = pd.DataFrame(datos[1:], columns=datos[0])

# Convertir las columnas numéricas a tipo float
df[df.columns[:-1]] = df[df.columns[:-1]].astype(float)

# Separar características y etiquetas
X = df.drop('species', axis=1)
y = df['species']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar un modelo de árbol de decisión
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Visualizar el árbol de decisión
plt.figure(figsize=(15,10))
tree.plot_tree(clf, feature_names=X.columns, class_names=df['species'].unique(), filled=True)
plt.show()