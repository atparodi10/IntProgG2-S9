# Solicita 10 números al usuario, guárdalos en una lista y muestra la suma total.
import time
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
numeros = []

for i in range(10):
    limpiar_pantalla()
    while True:
        try:
            print("Ingresa 10 números".center(50, "-"))
            n = int(input(f"Ingresa el numero {i+1}:"))
            numeros.append(n)
            break
            
            
        except ValueError:
            print("Error. Ingresa valores numéricos.")
            

suma = 0
# Suma recorriendo los valores de la lista
for numero in numeros:
    suma += numero

limpiar_pantalla()

print(f"La suma de los valores recorriendo los valores de la lista es de: {suma}")

# Suma con la función sum

print(f"La suma usando sum() es: {sum(numeros)}")