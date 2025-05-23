# Solicita al usuario 8 calificaciones, guárdalas en una lista y calcula el promedio.
import os


calificaciones = list()

for i in range(8):
    os.system('cls || clear')
    while True:
        try:
            print("Promedio de Calificaciones".center(50, "="))
            nota = float(input(f"Ingresa la califaicación {i+1}: "))
        
            if nota < 0 or nota > 100:
                print("Ingresa una calificación valida.")
            
            else:
                calificaciones.append(nota)
                break
                
        except ValueError:
            print("Ingrese valores numéricos.")

promedio = sum(calificaciones) / 8

os.system("cls || clear")
print("Promedio totol".center(30, "="))
print(f"Calificaciones: " + " - ".join(str(n) for n in calificaciones))
print(f"Promedio: {promedio: .2f}")        