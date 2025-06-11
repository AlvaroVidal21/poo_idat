

def calcular_interes(monto:float) -> float:

    if 10 <= monto <=  500:
        return 0.25
    elif 501 <= monto <= 1200:
        return 0.20
    elif 1201 <= monto <= 2000:
        return 0.15
    
    else:
        return None
    

def validar_monto(max_intentos=3):
    intentos = 0

    while intentos < max_intentos:
        try:
            monto = float(input("Ingrese el monto que desea solicitar: S/."))
            if 10 <= monto <= 2000:
                return monto
            else:
                print("Monto fuera de rango. Debe estar entre S/.10 y S/.2000.")
        
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")
        
        intentos += 1   

    raise ValueError("Número máximo de intentos alcanzado. Por favor, inténtelo más tarde.")



def calcular_monto_final(monto: float):
    interes = calcular_interes(monto)

    if interes is None:
        raise ValueError("Monto no cumple con los rangos establecidos.")
    
    total = monto + (monto*interes)
    return total