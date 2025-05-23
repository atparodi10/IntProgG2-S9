# Pide 10 números al usuario, guárdalos en una lista e imprímelos en orden inverso.
import os

numeros = []

for i in range(10):
    print("Ingresa 10 números".center(35, "="))
    os.system("cls || clear")
    while True:
        try:
            n = int(input(f"Ingresa el numero {i + 1}: "))
            numeros.append(n)
            break
        
        except ValueError:
            print("Ingresa datos numéricos.")
            

os.system("cls || clear")
print("Lista Original".center(30, "="))
print(" - ".join(str(n) for n in numeros))

print("\n")
numeros.reverse()
print("Lista Ordenada de manera Inversa". center(50, "="))
print(" - ".join(str(n) for n in numeros))