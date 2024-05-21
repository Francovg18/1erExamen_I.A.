'''8. Selecciones un grafo del AGENTE-VIAJERO con al menos 8 nodos, de 
los cuales obtenga todos los posibles caminos con Python (no solucione, 
solo obtenga todas las combinaciones).'''
from itertools import combinations

# Definir el grafo del agente viajero (lista de nodos)
nodos = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# Generar todas las combinaciones posibles de los nodos
for r in range(2, len(nodos) + 1):  # Desde 2 hasta el número total de nodos
    for combinacion in combinations(nodos, r):
        print(combinacion)
