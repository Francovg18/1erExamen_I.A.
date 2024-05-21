class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.padres = []
        self.hijos = []

    def agregar_padre(self, padre):
        self.padres.append(padre)

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

    def __str__(self):
        return f"{self.nombre} ({self.edad} años)"

# Definición de los miembros de la familia
abuelo = Persona("Antonio", 85)
abuela = Persona("Josefa", 80)
abuela2 = Persona("Nicola", 82)
padre = Persona("Damián", 50)
madre = Persona("Balvina", 48)
hijo1 = Persona("Ximena", 25)
hijo2 = Persona("Boris", 23)
hijo3 = Persona("Brayam", 20)

# Estableciendo relaciones familiares
padre.agregar_padre(abuelo)
padre.agregar_padre(abuela)
madre.agregar_padre(abuela2)

padre.agregar_hijo(hijo1)
padre.agregar_hijo(hijo2)
padre.agregar_hijo(hijo3)
madre.agregar_hijo(hijo1)
madre.agregar_hijo(hijo2)
madre.agregar_hijo(hijo3)

# Imprimiendo la estructura familiar
print("Abuelos:")
print(f"\t{abuelo}, {abuela}")
print(f"\t{abuela2}")

print("Padres:")
print(f"\t{padre}")
print(f"\t{madre}")

print("Hijos:")
print(f"\t{hijo1}")
print(f"\t{hijo2}")
print(f"\t{hijo3}")
