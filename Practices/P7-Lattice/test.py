from math import factorial


dimenciones = ["espacio", "tiempo", "precio", "tipo"]
result = []


def potencia(c):
    if len(c) == 0:
        return [[]]
    r = potencia(c[:-1])
    return r + [s + [c[-1]] for s in r]

def imprime_ordenado(c):
    for e in sorted(c, key=lambda s: (len(s), s)):
        print(e)


def combinaciones(c, n):
    return [s for s in potencia(c) if len(s) == n]



def numero_combinaciones(m, n):
    return factorial(m) // (factorial(n) * factorial(m - n))

imprime_ordenado(combinaciones(dimenciones, 3))
print(numero_combinaciones(4,2))

