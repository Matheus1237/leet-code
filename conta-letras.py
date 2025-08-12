# Contar quantas vezes cada letra aparece numa string

def conta_letras_repetidas(string):

    string = string.lower().replace(" ", "")

    quantidades = {}

    for l in string:
        if l not in quantidades:
            quantidades[l] = 1
        else:
            quantidades[l] += 1

    print(quantidades)

conta_letras_repetidas('aaaaaaAeeeeEiiiiiIuuuUooooO')
