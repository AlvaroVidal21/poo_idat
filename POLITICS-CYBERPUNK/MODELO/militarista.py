from MODELO.candidato import Candidato

class Militarista(Candidato):
    def __init__(self, nombre, edad, corporacion, porc_aprobacion, porc_corrupcion, porc_apoyo_militar):
        super().__init__(nombre, edad, corporacion, porc_aprobacion, porc_corrupcion)
        self.porc_apoyo_militar = porc_apoyo_militar

    # Override
    def puntaje_viabilidad(self):
        puntaje = super().puntaje_viabilidad()
        puntaje = puntaje * (1+(self.porc_apoyo_militar/100))
        return puntaje