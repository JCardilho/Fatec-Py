cont = "sim"
while cont == "sim" :
    num1 = float (input("DIGITE UM NUMERO: "))
    opcao = str (input("DIGITE A OPÇÃO :  +,  -,  *,  / "))
    num2 = float (input ("DIGITE OUTRO NUMERO: "))

    if opcao == "+":
        soma = num1 + num2
    elif opcao == "-" :
        soma = num1 - num2
    elif opcao =="*" :
        soma = num1 * num2
    elif opcao == "/" :
        soma = num1 / num2
    
    print("total :", soma)
    cont = str(input("QUER CONTINUAR EXECUTANDO DIGITE sim/ não :"))



