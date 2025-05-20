import os
import random
import time

def limpiar_pantalla():
    os.system('cls' if os.name=='nt' else 'clear')

participantes = []

while True:
    limpiar_pantalla()
    os.system("color a1")
    nombre = input("Ingrese su nombre(o 'Fin' para terminar con el programa): ").lower()
    if nombre == "fin":
        break
    
    participantes.append(nombre.capitalize())
    
    print("Participantes Agregados...")
    print(participantes)

for cont in range(10, 0, -1):
    os.system("cls || clear")
    print(cont)
    time.sleep(1)



print("Elemento agreagdos")
print(participantes)    

x = input("Presiona una tecla...")

limpiar_pantalla()

fin = len(participantes) - 1
ganador = random.randint(0, fin)
print("Ganador ", participantes[ganador])
    
    