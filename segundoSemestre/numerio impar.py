
somaprim = 0 


for i in range (0,10):
    num = int(input("Informe um numero: "))
    
    cont = 0
    
    for i in range (1,num+1):

        if num % i == 0:
            cont+= 1

    print(cont)
    if cont == 2:
        somaprim+= num
        print("È primo")
    else:
        print("Não é primo")
