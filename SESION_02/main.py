
from interfaz.interfaz import * 
from logica.logica import *






def run():

    ui_bienvenida()
    monto_solicitado =validar_monto()
    interes = calcular_interes(monto_solicitado)
    monto_final = calcular_monto_final(monto_solicitado)


if __name__ == "__main__":
    run()