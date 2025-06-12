import os
from utilidades.utils import *



def run():
    print("Bienvenido al Evaluador de Tareas")
    print("-" * 65)


    nombre = input("Nombre del estudiante: ")
    nota = input("Nota base (presiona Enter para usar 100): ")
    nota = int(nota) if nota.strip().isdigit() else 100


    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-" * 45)
    print(generar_mensaje(nombre, nota))
    print("-" * 45)     


    area = calcular_area_aprendizaje(nota)
    print(f"Área simbólica de tu aprendizaje: {area:.2f}")
    print("-" * 45)

    edad = pedir_entero("¿Cuál es tu edad? ")
    print(f"Tienes {edad} años. ¡A seguir aprendiendo!")
    print("-" * 45)


    emocion = input("¿Cómo te sientes con esta tarea?: ")
    transformar_emocion(emocion)

    print("¡Tarea completada con éxito!")

if __name__ == "__main__":
    run()