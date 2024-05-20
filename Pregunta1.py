'''
1. Seleccione un dataset de datos tabulares (UCI, KAAGLE). Realice lo siguiente:

   a. Con Python sin uso de librerías, calcule del ultimo cuartil, percentil 80 por columna; explique qué significa en cada caso.

   b. Realice lo mismo del inciso (a) con el uso de numpy y pandas

   c. Obtenga la media, mediana, moda y geométrica; explique la diferencia de los resultados y cuál de ellas se puede utilizar en un artículo científico.

   d. Grafique los datos y explique su comportamiento (PYTHON)
'''

import numpy as np
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv

# Cargar datos
datos = []
ruta_archivo = "C:/Users/Alex Choque/Downloads/iris.csv"

with open(ruta_archivo, newline='') as csvfile:
    lector = csv.reader(csvfile)
    for fila in lector:
        datos.append(fila)

# Mostrar las primeras filas del archivo
num_filas_mostrar = 5  

for fila in datos[:num_filas_mostrar]:
    print(fila)

print("****************************")

# Inciso a (sin usar librerías)
# Convertir columnas numéricas a flotantes
def convertir_a_flotante(columna):
    columna_convertida = []
    for valor in columna:
        try:
            valor_convertido = float(valor)
            columna_convertida.append(valor_convertido)
        except ValueError:
            pass #igno flotantes
    return columna_convertida

# Convertir las columnas numéricas a flotantes
columnas_numericas = [convertir_a_flotante(columna) for columna in zip(*datos[:-1])]

# Calcular el último cuartil y el percentil 80 de una columna
def calcular_cuartil_y_percentil(columna):
    columna_ordenada = sorted(columna)
    if not columna_ordenada:
        return None, None
    indice_ultimo_cuartil = int(0.75 * len(columna_ordenada))  
    indice_percentil_80 = int(0.8 * len(columna_ordenada))    

    ultimo_cuartil = columna_ordenada[indice_ultimo_cuartil]
    percentil_80 = columna_ordenada[indice_percentil_80]

    return ultimo_cuartil, percentil_80

# Calcular el último cuartil y el percentil 80 para cada columna numérica
resultados = {}
for i, columna in enumerate(columnas_numericas):
    ultimo_cuartil, percentil_80 = calcular_cuartil_y_percentil(columna)
    resultados[f'Columna {i+1}'] = {'Último Cuartil': ultimo_cuartil, 'Percentil 80': percentil_80}

# Impresión
for columna, valores in resultados.items():
    print(columna)
    print("Último Cuartil:", valores['Último Cuartil'])
    print("Percentil 80:", valores['Percentil 80'])
    print()

# Inciso B   
print("Inciso B")
# Convertir a DataFrame
df = pd.DataFrame(datos, columns=['largo_sépalo', 'ancho_sépalo', 'largo_pétalo', 'ancho_pétalo', 'especie'])

# Convertir columnas numéricas a flotantes
columnas_numericas = df.iloc[:, :-1].apply(pd.to_numeric, errors='coerce')

# Calcular el último cuartil y el percentil 80 usando Pandas
ultimo_cuartil = columnas_numericas.quantile(0.75)
percentil_80 = columnas_numericas.quantile(0.8)

# Imprimir los resultados
print("Último Cuartil:")
print(ultimo_cuartil)
print("\nPercentil 80:")
print(percentil_80)

# Inciso C
print("Inciso C")
datos_flotantes = []
for fila in datos:
    try:
        datos_flotantes.append([float(x) for x in fila[:4]])
    except ValueError:
        pass

# Transponer los datos para calcular las medidas estadísticas por columna
datos_transpuestos = np.array(datos_flotantes).T

# Calcular la media
media = np.mean(datos_transpuestos, axis=1)

# Calcular la mediana
mediana = np.median(datos_transpuestos, axis=1)

# Calcular la moda
moda = [Counter(columna).most_common(1)[0][0] for columna in datos_transpuestos]

# Calcular la media geométrica
media_geométrica = [np.prod(columna)**(1/len(columna)) for columna in datos_transpuestos]

# Imprimir resultados
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)
print("Media Geométrica:", media_geométrica)

# Inciso D
print("Inciso D")

# Convertir a DataFrame de Pandas
df = pd.DataFrame(datos, columns=['largo_sépalo', 'ancho_sépalo', 'largo_pétalo', 'ancho_pétalo', 'especie'])

# Convertir columnas numéricas a flotantes sin incluir la primera fila
columnas_numericas = df.iloc[1:, :-1].apply(pd.to_numeric, errors='coerce')

# Gráfico de dispersión usando Seaborn
sns.pairplot(columnas_numericas, markers=['o', 's', 'D'])

# Mostrar el gráfico
plt.show()



