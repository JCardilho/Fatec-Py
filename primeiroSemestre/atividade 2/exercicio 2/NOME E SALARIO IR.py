cont= 0
salario = 0
aliquota = 0
for cont in range(0,5):
    nome = str (input("DIGITE SEU NOME : "))
    salario= float(input("DIGITE O SÁLARIO BRUTO : "))
    print ("NOME:", nome)
    
    if salario < 600 :
        print ("ISENTO")
    else:
        if salario  < 1500 :
            aliquota= (salario *0.10)
        else:
             salario > 1500 
             aliquota= (salario *0.15)
        print ("VALOR ALIQUOTA DO IMPOSTO DE RENDA É: ",aliquota)
    




     
