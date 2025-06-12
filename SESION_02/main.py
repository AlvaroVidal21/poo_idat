
from interfaz.interfaz import * 
from logica.logica import *






def run():

    ui_bienvenida()

    
    monto_solicitado =validar_monto()


    if monto_solicitado is None:
        return None
    
    interes = calcular_interes(monto_solicitado)
    monto_final = calcular_monto_final(monto_solicitado)
    ui_resultado(monto_solicitado, interes, monto_final)


if __name__ == "__main__":
    run()