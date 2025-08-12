# Encontrar a subarray com maior soma

def encontra_subarray(numeros):

    maior_soma = numeros[0]
    soma_atual = numeros[0]

    for numero in numeros[1:]:
        soma_atual = max(numero, soma_atual + numero)
        maior_soma = max(maior_soma, soma_atual)

    return maior_soma


print(encontra_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))