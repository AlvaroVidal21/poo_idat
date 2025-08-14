
from CONTROLADOR.candidatos import get_candidatos




def run():
    candidatos = get_candidatos()
    for c in candidatos:
        print(c)
        print("-"*45)

if __name__ == '__main__':
    run()