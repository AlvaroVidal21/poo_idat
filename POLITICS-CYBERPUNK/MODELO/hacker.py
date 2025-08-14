from MODELO.candidato import Candidato


class Hacker(Candidato):
    def __init__(self, nombre, edad, corporacion, porc_aprobacion, porc_corrupcion, porc_net_runner):
        super().__init__(nombre, edad, corporacion, porc_aprobacion, porc_corrupcion)
        self.porc_net_runner = porc_net_runner


    # Override
    def puntaje_viabilidad(self):
        puntaje = super().puntaje_viabilidad()
        puntaje = puntaje * (1+(self.porc_net_runner/100))
        return puntaje