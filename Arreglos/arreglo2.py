print("\n")
arreglo_str = ["uno", "dos", "tres", "cuatro", "cinco"]

# insertar un elemento
arreglo_str.insert(0, "cero")

print(arreglo_str)
print("\n")
# Contar cunatos elemntos tiene un arreglo

print("El arreglo tiene ",len(arreglo_str), "elementos")

print("\n")
# eliminar un elemnto

arreglo_str.remove("tres")

print(arreglo_str)
print("\n")
# eliminar elemnto por posicón

arreglo_str.pop(2)

print("Array de cadenas despues de eliminar el elemento en la posición 2: ", arreglo_str)
print("\n")