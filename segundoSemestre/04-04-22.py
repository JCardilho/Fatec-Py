#uma empresa de onibus prescisa de um sistema para facilitar a venda passagens.
#O onibus possui 40 lugares e usuario pode escolher a poltrona informando um
#numero de 1 a 40, se a poltrona estiver ocupada , devera ser exibido uma
#mensagem informando que a poltrona esta ocupado caso contrario a poltrona
#deve ser reservada.O sistema deve ser encerrado quando for digitado zero no
#numero da poltrona. No final deve ser digitado  na tela:
#a quantitade de poltrona ocupada
#a quantidade de poltrona livre

lista = []
cont = 0 
num=1


for i in range(0,40):
    lista.append(0)
print("-"*30)

while num != -1:
    num=(int(input("digite a poltrona desejado (1 - 40): ")))
    num-= 1
    
    if num != -1:
        if (num >= 0) and (num <= 39):
        
            if (lista[num] == 0):
                lista[num]= 1
                cont+=1
                print("Reserva realizada com sucesso")
                print("-"*30)
            
            elif (lista[num] == 1):
                print ("Poltrona ocupado")
                print("-"*30)

        else:
            print("Valor invalido")
            print("-"*30)

print("-"*30)
print( f"A quantidade de poltrona ocupada: {cont}")
print(f"A quantidade de poltrona vazia: {40 - cont} ")
