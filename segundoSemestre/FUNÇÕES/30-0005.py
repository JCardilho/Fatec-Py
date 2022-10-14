#execicio 3 slide

def soma(n1,n2):
    total=0
    if n1 < n2:
        for i in range (n1,n2+1):
            total+=i
    else:
        for i in range (n2,n1+1):
            total+=i

    return total

print ("programa principal")
num1= int (input( "entre com um numero"))
num2= int (input( "entre com segundo numero"))
res=soma (num1,num2)
print (f"A SOMA entrenumero  {num1} e o numero  {num2} é: {res}")
print (" terminou a execução")
