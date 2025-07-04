from Controlador.controlador import procesar_todos

def mostrar_menu():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Operaciones Trigonométricas")
    print("2. Operaciones de Sumatoria")
    print("3. Operaciones Aritméticas")
    print("4. Comparar Mayor/Menor")
    print("5. Todas las Operaciones")
    print("0. Salir")

    while True:
        opcion = input("Seleccione una opción: ")
        if opcion in ["0", "1", "2", "3", "4", "5"]:
            return int(opcion)
        print("❌ Opción inválida. Intente nuevamente.")

def solicitar_numeros():
    print("\n📥 Ingrese 3 números para procesar:")
    while True:
        try:
            n1 = float(input("Número 1: "))
            n2 = float(input("Número 2: "))
            n3 = float(input("Número 3: "))
            return n1, n2, n3
        except ValueError:
            print("❌ Error: Ingrese solo números.")

def mostrar_resultados(resultados, opcion):
    print("\n🧾 RESULTADOS")
    print("-" * 40)

    # Diccionario de filtros según la opción
    filtros = {
        1: ['logaritmo10', 'tangente', 'contangente'],
        2: ['sumatoria', 'cuadrados', 'cubos'],
        3: ['media', 'promedio', 'moda'],
        4: ['mayor', 'menor'],
        5: list(resultados.keys())  # todo
    }

    for clave, valor in resultados.items():
        if clave in filtros[opcion]:
            print(f"{clave.capitalize():<20}: ", end="")
            if type(valor) == list:
                print(", ".join(str(round(v, 4)) if isinstance(v, float) else str(v) for v in valor))
            else:
                print(round(valor, 4) if isinstance(valor, float) else valor)
    print("-" * 40)

def run():
    while True:
        opcion = mostrar_menu()
        if opcion == 0:
            print("👋 Gracias por usar el sistema. ¡Hasta pronto!")
            break

        n1, n2, n3 = solicitar_numeros()
        resultados = procesar_todos(n1, n2, n3)
        mostrar_resultados(resultados, opcion)

if __name__ == '__main__':
    run()
