def mdc(numeros):
    if len(numeros) == 1:
        return (numeros[0])



   if numeros[0] == 0:
        numeros.remove(0)
        return (mdc(numeros))



   resto = numeros[1] % numeros[0]
    numeros[1] = numeros[0]
    numeros[0] = resto
    return (mdc(numeros))



listNumeros = []
for n in range(3):
    listNumeros.append(int(input(f'Informe o {n+1}º número: ')))



listNumeros.sort()
tuplaNumeros = tuple(listNumeros)



resultMDC = mdc(listNumeros)
print(f'O MDC entre os números {tuplaNumeros} é: {resultMDC}')
