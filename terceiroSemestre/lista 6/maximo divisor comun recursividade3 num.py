def mdc1(num1,num2):
    while(num2):
        num1,num2=num2,num1%num2
    return num1

def mdc(numero):

    if len(numero) == 2:
        return mdc1(numero[0], numero[1])
    else:
        mdc2 = mdc1(numero[0], numero[1])
        numero[0] = mdc2
        del numero[1]
        return mdc(numero)
num1=int (input ("Digite o primeiro numero para o MDC :"))
num2=int (input ("Digite o segundo numero para o MDC :"))
num3=int (input ("Digite o terceiro numero para o MDC :"))
result=mdc([num1,num2,num3])
print (f"O MDC DE {num1,num2,num3} É : {result }")
