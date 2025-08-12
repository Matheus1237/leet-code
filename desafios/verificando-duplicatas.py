# Verificando duplicadas em uma lista

def verifica_duplicatas(lista):

    qtd_lista = {}
    lista_duplicadas = []

    for n in lista:
        if n not in qtd_lista:
            qtd_lista[n] = 1

        else:
            qtd_lista[n] += 1

            if qtd_lista[n] == 2:
                lista_duplicadas.append(n)

    return lista_duplicadas




print(verifica_duplicatas([2, 2, 5, 1, 2, 3, 5, 1]))