#10.- Realice en Python la impresión de ¨hola mundo¨.
import sys

def print_char(c):
    sys.stdout.write(c)
    sys.stdout.flush()

def hola_mundo():
    mensaje = "Hola mundo"
    for letra in mensaje:
        print_char(letra)
    print_char('\n')

hola_mundo()

print("Hola mundo")
