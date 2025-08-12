# Verificar se uma palavra é um palíndromo

def eh_palindromo(palavra):

    palavra = palavra.lower().replace(" ", "")

    if palavra[::-1] == palavra:
        print('É um palíndromo!')

    else:
        print('Não é um palíndromo!')

    return palavra



print(eh_palindromo('Ana'))
