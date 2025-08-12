# Contar vogais

def conta_vogais(string):

    string_formatada = string.lower().replace(" ", "")
    qtd_vogais = 0

    for l in string_formatada:
        if l in "aeiouáéíóú":
            qtd_vogais += 1

    return qtd_vogais


print(conta_vogais("Meu nome é Matheus"))