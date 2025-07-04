

def media_arimetica(n1: float, n2: float, n3: float) -> float:
    return (n1 + n2 + n3) / 3


def promedio(n1: float, n2: float, n3: float) -> float:
    return media_arimetica(n1, n2, n3) # Lo mismo que media aritmetica


def moda(n1: float, n2: float, n3: float) -> float:
    if n1 == n2 and n1 == n3:
        return n1
    elif n1 == n2:
        return n1
    elif n1 == n3:
        return n1
    elif n2 == n3:
        return n2
    else:
        return 'No hay moda' 