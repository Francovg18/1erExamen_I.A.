import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, OrdinalEncoder, MinMaxScaler

# Cargar el dataset desde la ruta proporcionada
ruta_archivo = "C:/Users/Alex Choque/Downloads/iris.csv"
datos = pd.read_csv(ruta_archivo)

'''
1.-Imputación de valores faltantes: Se utiliza para manejar datos incompletos y
 evitar que los algoritmos de machine learning se vean afectados por valores 
 faltantes.
'''
imputer = SimpleImputer(strategy='mean')
datos[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']] = imputer.fit_transform(datos[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']])

'''
2.- OneHotEncoder: Convierte variables categóricas en variables binarias, permitiendo
a los modelos interpretar correctamente las categorías sin asumir un orden entre
ellas.
'''
encoder = OneHotEncoder(sparse=False)
species_encoded = encoder.fit_transform(datos[['species']])
species_df = pd.DataFrame(species_encoded, columns=encoder.get_feature_names_out(['species']))
datos = pd.concat([datos, species_df], axis=1).drop('species', axis=1)

'''
3.- Escalado estándar (StandardScaler): Normaliza las características para que todas 
tengan media 0 y desviación estándar 1, mejorando el rendimiento de muchos 
algoritmos de machine learning.
'''
scaler = StandardScaler()
datos[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']] = scaler.fit_transform(datos[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']])

# Añadir una columna categórica ficticia para la demostración
datos['flower_rank'] = ['low', 'medium', 'medium', 'high', 'medium', 'high', 'low', 'medium', 'low', 'high'] * (len(datos) // 10)

'''
4.- Codificación ordinal (OrdinalEncoder): Convierte variables categóricas en números
 enteros, preservando el orden natural de las categorías.
'''
ordinal_encoder = OrdinalEncoder(categories=[['low', 'medium', 'high']])
datos[['flower_rank']] = ordinal_encoder.fit_transform(datos[['flower_rank']])

'''
Normalización (MinMaxScaler): Escala las características a un rango específico,
típicamente entre 0 y 1, lo que puede ser útil para algoritmos que requieren un 
rango de entrada específico.
'''
min_max_scaler = MinMaxScaler()
datos[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']] = min_max_scaler.fit_transform(datos[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']])

print(datos.head())


