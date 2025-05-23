# Dada una lista de 10 números, contar cuántos son mayores que 50.

numeros = [12, 7, 54, 63, 28, 91, 33, 5, 76, 49]

contador = 0

for i in numeros:
    if i > 50:
        contador += 1

mayores = [n for n in numeros if n > 50]
print(" Lista de números ".center(30, "="))
print(" - ".join(str(n) for n in numeros))
print("\n")
print(f"Hay un total de {contador} de números mayores a 50")
print("\n")
print(" Lista de numeros mayores a 50 ".center(50, "="))
print(" - ".join(str(n) for n in mayores))