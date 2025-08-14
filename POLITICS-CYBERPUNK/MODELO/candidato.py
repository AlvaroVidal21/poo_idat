class Candidato:
    def __init__(self, nombre, edad, corporacion, porc_aprobacion, porc_corrupcion):
        self.nombre = nombre
        self.edad = edad
        self.corporacion = corporacion
        self.porc_aprobacion = porc_aprobacion
        self.porc_corrupcion = porc_corrupcion


    def puntaje_viabilidad(self):
        puntaje = self.porc_aprobacion * (1 - (self.porc_corrupcion / 100))
        return puntaje


    def __str__(self):
        return f"{self.nombre} [*] Corp: {self.corporacion}\nAprobacion: {self.porc_aprobacion} % [*] Corrupcion: {self.porc_corrupcion} %\nViabilidad: {self.puntaje_viabilidad():.2f} %"

    
    
"""
El puntaje de viabildidad en las clases hijas se le agregará como adicionaal su virtud.
Por ejemplo: Militarista: puntaje * (1+(porc_apoyo_militar/100))
"""