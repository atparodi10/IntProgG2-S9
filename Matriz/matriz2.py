from tabulate import tabulate

matriz = [["Diego","Victor", "Lucas"], ["Carlos", "Juan", "Hector"], ["Steven", "Edmundo", "Henry"]]

cant_letras = []

for fila in matriz:
    nueva_fila = []
    for columna in fila:
        nueva_fila.append(len(columna))
    cant_letras.append(nueva_fila)
        


print(tabulate(matriz, tablefmt="grid"))
print(tabulate(cant_letras, tablefmt="grid"))