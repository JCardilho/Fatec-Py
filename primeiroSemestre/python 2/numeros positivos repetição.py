
cont = 1
while  cont <= 3 :
   
    cod = int( input("DIGITE O CODIGO DO PRODUTO : "))
    prod = str(input("DIGITE O PRODUTO: "))
    preco = float(input("DIGITE O PREÇO UNITARIO: "))
    quant = int(input("DIGITE A QUANTIDADE: "))
    print("--------------------------------")
    
    total = quant * preco

    if total >= 100:
        descont = total *0.1
    else:
        descont = total * 0.05
    totalcompra = total - descont
    
    print("Desconto",descont)
    print("O valor da compra é:", totalcompra)
    print("--------------------------------")
    cont = cont + 1

