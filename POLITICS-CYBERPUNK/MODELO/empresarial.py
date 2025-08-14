from MODELO.candidato import Candidato

class Empresarial(Candidato):
    def __init__(self, nombre, edad, corporacion, porc_aprobacion, porc_corrupcion, porc_apoyo_empresarial):
        super().__init__(nombre, edad, corporacion, porc_aprobacion, porc_corrupcion)
        self.porc_apoyo_empresarial = porc_apoyo_empresarial


    def puntaje_viabilidad(self):
        puntaje = super().puntaje_viabilidad()
        puntaje = puntaje * (1+(self.porc_apoyo_empresarial/100))
        return puntaje