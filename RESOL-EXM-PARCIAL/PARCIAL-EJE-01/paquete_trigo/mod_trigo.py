import math

def logaritmo10(n1: float, n2: float, n3: float) -> float:
    try:
        # Uusamos list comprehension
        return [math.log10(n) for n in [n1, n2, n3]]
    except ValueError as e:
        return 'No se puede calcular el logaritmo'
    

def  tangente(n1: float, n2: float, n3: float) -> float:
    # Ojito, tangente usa radianes, tons convertimos grados a radianes
    try:
        # Lis comprehhesion
        return [math.tan(math.radians(n)) for n in [n1, n2, n3]]
    
    except ValueError as e:
        return 'No se puede calcular el tangente'
    

"""
contangete(x) = 1/tangente(x); donde tangente(x) no puede ser 0, obvio

"""

def contangente(n1: float, n2: float, n3: float) -> float:
    
    lista_resultados = []
    
    for n in [n1, n2, n3]:
        radian_n = math.radians(n)

        try:
            cont_n = 1 / math.tan(radian_n)
            lista_resultados.append(cont_n)

        except ZeroDivisionError:
            lista_resultados.append('Indefinido')

    return lista_resultados




