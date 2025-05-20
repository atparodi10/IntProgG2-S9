array_int = [5, 4, 9, 2, 1]

print(f"Array de enteros: {array_int}")

array_int.sort()

print("Array de enteros ordenados: ", array_int)

array_int.sort(reverse=True)

print("Lista odenada: ", array_int)

elemento = 4

if elemento in array_int:
    print(f"El elemnto {elemento}, estan dentro del array")

else:
    print("EL elemento no esta dentro de la lista.")
    

array_int.append(6)

print(f"array despues de insertar el elemento 6: {array_int}")