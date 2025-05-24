from tabulate import tabulate

precios = []

for i in range(3):
    cantidad = []
    for j in range(3):
        precio = float(input(f"Ingresa el precio del producto {i}.{j}: "))
        cantidad.append(precio)
    precios.append(cantidad)

aumento = []

for fila in precios:
    porcentaje = []
    for precio in fila:
        descuento = (0.15 * precio) + precio
        porcentaje.append(descuento)
    
    aumento.append(porcentaje)


print(tabulate(precios, tablefmt="grid"))
print(tabulate(aumento, headers=["Precio con 15%", "Precio con 15%", "Precio con 15%"], tablefmt="grid"))
        