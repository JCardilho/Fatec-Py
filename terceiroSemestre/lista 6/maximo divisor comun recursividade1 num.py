def mdc(numeros):
    if len(numeros) == 1:
        return (numeros[len(numeros) - 1])



   if numeros[len(numeros) - 1] == 0:
        numeros.remove(0)
        return (mdc(numeros))



   resto = numeros[len(numeros) - 2] % numeros[len(numeros) - 1]
    numeros[len(numeros) - 2] = numeros[len(numeros) - 1]
    numeros[len(numeros) - 1] = resto
    return (mdc(numeros))



listNumeros = []
for n in range(3):
    listNumeros.append(int(input(f'Informe o {n+1}º número: ')))



listNumeros.sort()
listNumeros.reverse()
tuplaNumeros = tuple(listNumeros)



resultMDC = mdc(listNumeros)
print(f'O MDC entre os números {tuplaNumeros} é: {resultMDC}')
