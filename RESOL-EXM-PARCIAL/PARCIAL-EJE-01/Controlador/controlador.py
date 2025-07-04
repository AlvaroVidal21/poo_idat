from paquete_arimetica.mod_aritmetica import media_arimetica, promedio, moda
from paquete_may_men.mod_may_men import mayor, menor
from paquete_sumatoria.mod_sumatorias import sumatoria, cuadrados, cubos
from paquete_trigo.mod_trigo import logaritmo10, tangente, contangente


def procesar_todos(n1: float, n2: float, n3: float) -> float:
    return {
        'media': media_arimetica(n1, n2, n3),
        'promedio': promedio(n1, n2, n3),
        'moda': moda(n1, n2, n3),
        'sumatoria': sumatoria(n1, n2, n3),
        'cuadrados': cuadrados(n1, n2, n3),
        'cubos': cubos(n1, n2, n3),
        'logaritmo10': logaritmo10(n1, n2, n3),
        'tangente': tangente(n1, n2, n3),
        'contangente': contangente(n1, n2, n3),
        'mayor': mayor(n1, n2, n3),
        'menor': menor(n1, n2, n3)  
    }