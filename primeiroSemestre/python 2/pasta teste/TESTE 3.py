cont = 0
while cont < 3:
    cont = cont + 1
    preco = float(input("DIGITE O PREÇO UNITARIO: "))
    quant = int(input("DIGITE A QUANTIDADE: "))
    total = quant * preco

    print("-------------",cont,"-------------------",  total)
