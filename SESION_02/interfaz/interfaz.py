

def ui_bienvenida():
    print("-"*50)
    print(" "*8, "SOFTWARE DE PRESTAMOS SIMPLES")
    print("-"*50)


def ui_resultado(monto_solicitado:float, interes:float, monto_final:float):
    print("-"*50)
    print(" "*8, "RESULTADO DEL PRESTAMO")
    print("-"*50)
    print(f"Monto solicitado: S/.{monto_solicitado:.2f}")
    print(f"Interes: S/.{interes:.2f}")
    print(f"Monto final a pagar: S/.{monto_final:.2f}")
    print("-"*50)   