from random import randint
vogais = ['A', 'E', 'I', 'O', 'U', 'À', 'Ã', 'Â', 'Á', 'É', 'Ê', 'Í', 'Ô', 'Õ', 'Ó', 'Ú']

def contarPalavras(frase):
    frase = frase.split()
    return (len(frase))

def contarVogais(frase):
    cont = 0
    for letra in frase:
        if letra in vogais:
            cont += 1
    return (cont)

def contarConsoantes(frase):
    cont = 0
    for letra in frase:
        if ord(letra) >= 65 and ord(letra) <= 90 and letra not in vogais:
            cont += 1
    return (cont)

def concatenarFrase(frase):
    for x in range(3):
        frase = str(randint(1,9)) + frase + chr(randint(65, 90))
    return (frase)

def cifrarFrase(frase):
    for l in range(len(frase)):
        if frase[l].upper() in vogais:
            frase[l] = chr(ord(frase[l]) + 4)
        if ord(frase[l].upper()) >= 65 and ord(frase[l].upper()) <= 90 and frase[l].upper() not in vogais:
            frase[l] = chr(ord(frase[l]) - 5)
    cifra = ''.join(frase)
    return (cifra)

fraseOriginal = input('Informe uma frase: ')
fraseNova = concatenarFrase(fraseOriginal)
fraseCifrada = cifrarFrase(list(fraseNova))

print(f'A frase contém {len(fraseOriginal)} caracteres!')
print(f'A frase contém {contarPalavras(fraseOriginal.upper())} palavras!')
print(f'A frase contém {contarVogais(list(fraseOriginal.upper()))} vogais!')
print(f'A frase contém {contarConsoantes(list(fraseOriginal.upper()))} consoantes!')
print(f'Frase original: "{fraseOriginal}"')
print(f'Frase concatenada: "{fraseNova}"')
print(f'Frase concatenada cifrada: "{fraseCifrada}"')

''' EXERCÍCIO MANIPULAÇÃO DE STRING
 - Informe uma frase;
 - Exiba quantos caracteres tem a frase;
 - Exiba o número de vogais;
 - Exiba o número de consoantes;
 - Exiba o Número de Palavras;
 - Acrescente 3 números no iníco da frase;
 - Acrescente 3 letras no fim da frase;
 - Exiba a frase;
 - Faça a cifra somando mais 4 para as vogais e
 menos 5 para os outros caracteres;
 - Apresente a frase original seguida da frase cifrada.
'''