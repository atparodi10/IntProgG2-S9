# Dada una lista de palabras, solicita al usuario una palabra y muestra si está o no en la lista.

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


palabras = [
    "gato", "perro", "casa", "árbol", "luz",
    "sol", "luna", "estrella", "mar", "montaña",
    "río", "flor", "nube", "cielo", "pájaro",
    "camino", "puerta", "ventana", "fuego", "tierra"
]

while  True:
    cls()
    print("Ingresa la palabra o fin para terminar con la busqueda de la palabra.")
    cadena = input("Ingresa una palabra para buscarla en la lista: ").lower()
        
    if cadena == "fin":
        print("Saliendo del programa...")
        input("Presiona enter para salir...")
        break
        
    if cadena in palabras:
        print(f"La palabra {cadena} esta dentro de la lista.")
    else:
        print(f"La palabra {cadena} no esta dentro de la lista")
    
    input("Presiona enter para continuar...")
        
    
    

