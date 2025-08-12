# Verificar se duas palavras são anagramas

# Solução 01

def verifica_anagramas(palavra1, palavra2):

    palavra1 = palavra1.lower().replace(" ", "")
    palavra2 = palavra2.lower().replace(" ", "")

    palavralist1 = []
    palavralist2 = []

    for l in palavra1:
        palavralist1.append(l)

    for l in palavra2:
        palavralist2.append(l)

    palavralist1.sort()   
    palavralist2.sort()

    if palavralist1 == palavralist2:
        print("É um anagrama")

    return palavralist1, palavralist2

print(verifica_anagramas('amor', 'roma'))

# Solução 02

def verifica_anagrama(p1, p2):

    p1 = p1.lower().replace(" ", "")
    p2 = p2.lower().replace(" ", "")

    if sorted(p1) == sorted(p2):
        return True
    
    return False

print(verifica_anagrama("amor", "roma"))