def primo (num):
    contdiv=0
    for k in range (1,num+1):
        if num % k ==0:
            contdiv+=1

    if contdiv==2:
        print (f"o numero {num} é primo")
    else:
        print ("não é primo")
print ("programa principal")
n1= int (input(" entre com um numero"))

primo(n1)
print ("terminou a execução")
    
