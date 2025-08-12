# Média, Moda e Mediana de uma lista

def media_moda_mediana(numeros):

    print(numeros)

    # Media

    media = sum(numeros) / len(numeros)

    numeros_quant = {}

    for n in numeros:
        if n not in numeros_quant:
            numeros_quant[n] = 1
        else:
            numeros_quant[n] += 1
    
    print(media)

    # Moda

    maior_freq = 0

    for freq in numeros_quant.values():
        if freq > maior_freq:
            maior_freq = freq

    moda = []

    for num, freq in numeros_quant.items():
        if freq == maior_freq:
            moda.append(num)

    print(moda)

    # Mediana

    numeros = sorted(numeros)
    meio = len(numeros) // 2

    if len(numeros) % 2 != 0:
        mediana = numeros[meio]
    
    else:
        mediana = (numeros[meio - 1] + numeros[meio]) / 2

    print(mediana)

    print(f"Ordenada - {numeros}")




media_moda_mediana([7, 8, 5, 5, 3, 9, 10, 2])



