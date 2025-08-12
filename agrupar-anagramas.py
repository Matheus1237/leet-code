# Agrupar anagramas em uma lista

def agrupa_anagramas(palavras):

    grupos = {}

    for p in palavras:
        chave = "".join(sorted(p))

        if chave not in grupos:
            grupos[chave] = []

        grupos[chave].append(p)

    print(grupos)


agrupa_anagramas(["amor", "roma", "carro", "arco", "corra", "maro"])