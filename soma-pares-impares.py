# Soma de pares e ímpares de uma lista

# Solução 01

def soma_numeros_pares_impares(numeros):

    pares = []
    impares = []

    for n in numeros:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)

    sum_pares = sum(pares)
    sum_impares = sum(impares)
    

    print(f"Soma dos números pares: {sum_pares}")
    print(f"Soma dos números ímpares: {sum_impares}")
    
    return pares, impares

print(soma_numeros_pares_impares([2, 4, 6, 1, 3, 5]))

# Solução 02

def soma_numeros_pares_impares_s2(numeros):

    pares = 0
    impares = 0

    for n in numeros:
        if n % 2 == 0:
            pares += n
        else:
            impares += n

    return pares, impares

print(soma_numeros_pares_impares_s2([2, 4, 6, 1, 3, 5]))
