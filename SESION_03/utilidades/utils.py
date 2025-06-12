import math

def generar_mensaje(nombre: str, nota: int = 100) -> str:
    return f"Hola {nombre}, tu nota base registrada es {nota}."

def calcular_area_aprendizaje(valor: float) -> float:
    return math.pi * valor ** 2

def pedir_entero(mensaje: str) -> int:
    try:
        return int(input(mensaje))
    except ValueError:
        print("⚠️ Entrada inválida. Se usará 0.")
        return 0

def transformar_emocion(palabra: str):
    print("Procesando tu emoción...")
    print(f"🔹 Original     : '{palabra}'")
    print(f"🔹 Mayúsculas   : '{palabra.upper()}'")
    print(f"🔹 Capitalizado : '{palabra.capitalize()}'")
    print(f"🔹 Sin espacios : '{palabra.strip()}'")