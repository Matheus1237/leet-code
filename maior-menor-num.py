# Maior e menor número em uma lista

def encontra_maior_menor_numero(numeros):

    maior = numeros[0]
    menor = numeros[0]

    for n in numeros:
        if n > maior:
            maior =  n
        if n < menor:
            menor = n
    
    return f"Maior = {maior} - Menor = {menor}"

print(encontra_maior_menor_numero([4, 6, 1, 7, 50]))
