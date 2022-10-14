#enunciado

par=0
inf10=0

for i in range (0,10) :
    n=int (input("DIGITE UM NUMERO"))
    if n % 2 ==0 :
        par=par + n
    if n < 10 :
        inf10+=1
   
print ("A SOMADOS PARE :" , par)
print (" QUANTIDADE DE NUMEROS INF10 :", inf10)
