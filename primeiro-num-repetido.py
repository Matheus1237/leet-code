# Econtrar o primeiro número que aparece mais de uma vez

def encontra_primeiro_repetido(numeros):

    vistos = set()

    for n in numeros:
        if n in vistos:
            return n

        else:
            vistos.add(n)

    return None

print(encontra_primeiro_repetido([2, 5, 1, 7, 3, 5, 1]))
