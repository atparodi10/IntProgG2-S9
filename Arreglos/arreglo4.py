# Crear una lista manualmente y mostrar su contenido
import os
import time 

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


for i in numero:
    limpiar_pantalla()
    print("Elementos de la lista...")
    print(i)
    time.sleep(1)
    
print(" Elementos de la lista ".center(50, "="))
print(numero)
print("\n")
print("Elementos con formato de impresión".center(50, "="))

print("-".join(str(n) for n in numero))