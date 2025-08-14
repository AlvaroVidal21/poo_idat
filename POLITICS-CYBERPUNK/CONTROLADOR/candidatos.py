# Importamos los modelos
from MODELO import Militarista, Empresarial, Hacker

# Nombre, edad, corporacion, % aprob, % corrupcion, %virtud

candidatos = [
    Militarista("Lucius Kroll", 54, "Arasaka", 20, 20, 40),
    Hacker("Mara Cipher", 31, "NetWatch", 65, 25, 55),
    Empresarial("Viktor Crane", 48, "Militech", 80, 30, 35)
]



def get_candidatos():
    return sorted(candidatos, key=lambda c: c.puntaje_viabilidad(), reverse=True)