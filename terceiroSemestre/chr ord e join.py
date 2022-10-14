vogais = ['A', 'E', 'I', 'O', 'U', 'À', 'Ã', 'Â', 'Á', 'É', 'Ê', 'Í', 'Ô', 'Õ', 'Ó', 'Ú']
def cifrarFrase(frase):
    print (frase)
    for l in range(len(frase)):
        if frase[l].upper() in vogais:
            frase[l] = chr(ord(frase[l]) + 4)#chr retorna letra conforme tabela ascii
            # ord tranforma a letra em numero da tabela ascii
        elif ord(frase[l].upper()) >= 65 and ord(frase[l].upper()) <= 90 and frase[l].upper() not in vogais:
            frase[l] = chr(ord(frase[l]) - 5)
    cifra = ''.join(frase)# junta a lista
    print (cifra)
    return (cifra)
frase = input('Informe uma frase: ')    
a=cifrarFrase(list(frase))
print (a)
