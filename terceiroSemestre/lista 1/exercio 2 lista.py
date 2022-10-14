#02)De acordo com o texto abaixo crie um algoritmo usando funções.
#O senhor Airton tem uma loja de roupas e calçados situada na cidade de Conchas,
#ele vende noatacado e varejo tendo situações diferentes para cada situação,
#sendo que normalmente seuprocedimento de vendas tem sido o seguinte:Na compra
#de calçados no varejo ele faz a seguinte verificação:Consulta o cliente-Se o
#cliente é devedor, vende a mercadoria somente à vista-Se o cliente é adimplente
#(paga em dia),então oferece as seguintes condições:-Se o cliente vai comprar a
#vista-Se for a dinheiro então-Concede 20% de desconto-Se for em cheque então-
#Concede15% de desconto-Se o cliente vai comprar a prazo ele oferece as seguinte
#s condições:-Se comprar em duas vezes então:-Conceder 5% de desconto-Se comprar
#em três vezes então-Não conceder desconto-Se comprar em quatro ou mais vezes
#então-5% de acréscimo no valor total da venda
#Utilize pelo menos duas funções.



lista=["JOAO","ANTONIO","FERNANDO","ANTUNES","FELIPE", "MARIA","SILVANA"]

def clidev(nome, compra):
    print(f"{nome} efetuou uma compra no Valor :  {compra}")
    print("autorizado somente venda a vista")
    
    opcao= (input("pagamento em dinheiro digite'1', para pagamento em cheque'2'"))
    if opcao=="1":
        topagar=(compra*.20)
        topagar1=compra - topagar
        print (f"  total de desconto  20 %  {topagar}")
        print (f"Valor a pagar em dinheiro com 20 % de desconto {topagar1:,.2f}")
    else:
        topagar=(compra*.15)
        topagar1=compra - topagar
        print (f"  total de desconto  15 %  {topagar}")
        print (f"Valor a pagar em dinheiro com 15 % de desconto {topagar1:,.2f}")
        
def cliadim(nome,compra):
    verificador = False
    print("autorizado venda a prazo")
    while (verificador == False):    
        opcao=int(input("digite '2' pagamento em duas vezes, '3' em tres vezes,'4' para quatro vezes ou mais: "))
        if opcao >=2 and opcao <=4 :
            verificador = True
            if opcao ==2:
                topagar=(compra*.05)
                topagar1= compra - topagar
                topagar2=topagar1 / 2
                print (f"  total a pagar com5% de desconto  {topagar1:,.2F}")
                print (f"Valor a pagar em 2 vezes de : {topagar2:,.2f}")
            elif opcao ==3:
                topagar=compra/3
                print (f"  total a pagar sem desconto  {compra:,.2F}")
                print (f"Valor a pagar em 3 vezes de : {topagar:,.2f}")
            elif opcao ==4:
                verificador1 = False
                while (verificador1 == False):        
                    num=int(input("Digite o numero de parcelas que deseja de 4 a 10:"))
                    if num >=4 and num <=10:
                        verificador1 = True       
                        topagar=(compra*.05)
                        topagar1= compra + topagar
                        topagar2=topagar1/num
                        print (f"total a pagar com acrecimo de 5% : {topagar1:,.2F}")
                        print (f"Valor a pagar em { num } vezes de : {topagar2:,.2f}")
                    else:
                        print ("OPÇÃO INVALIDA...")
                        verificador1 = False
        else:
            print ("OPÇÃO INVALIDA...")
            verificador == False

nome=str(input("Digite um nome para consulta  : "))
nome = nome.upper()
compra=float(input("Digite o valor da compra  :"))
if nome in lista:
    clidev(nome, compra)
    
else:
    cliadim(nome,compra)
