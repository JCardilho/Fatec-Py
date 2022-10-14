#03)Elaborar um algoritmo para realizar o cálculodo salário líquidode um
#determinado funcionário. Para tal, insira o nome do funcionário o valor/hora, a
#quantidade de horas trabalhadas, um  valor de  deslocamento  multiplicando  o
#valor  de quilômetrosrodados pelo valor 0,51 e o tipo de contratação que terá o
#s seguintes critérios:•Se o funcionário for contratado como pessoa jurídica,adi
#cionar 30% no totale  disparar  uma  mensagem  dizendo  que  o  valor  do  INSS
#será recolhido pelo funcionário;
#•Se  o  funcionário  for  contratado  como  pessoa  física,descontar  6%do
#total;•Se  o  funcionário  for  contratado  com  carteira  assinada(CLT),
#adicionar 8%  de periculosidade e descontar 5% de INSS do total.Por fim,
#apresenteas seguintes informações na tela:
#•Nome do funcionário: xxxxxxxxxx      •Total deslocamento: xxxxxxxxx
#•Total salário valor hora: xxxxxxxx   •Total salário bruto: xxxxxxxxxxx
#•Total descontos: xxxxxxxxxxxx        •Total salário líquido: xxxxxxxxx
#Utilize pelo menos 3 funções.

def op1(nome, vhora,thora,desloc,opcao):
    desloc= desloc*0.51 + desloc 
    total=vhora*thora+desloc 
    total1=total*0.30
    total2=total1+total
    print("=-=-"*20)
    print(f"Nome do Funcionario : {nome}") 
    print(f"Total de deslocamento :  {desloc}")
    print(f"valor da hora :{vhora}")
    print (f"total salario bruto : {total2}")
    print(f"Total de desconto :   00000")
    print (f"total salario liquido : {total2}")
    print (f" O valor do INSS {total1} devera ser recolhido pelo funcionario")     

def op2(nome, vhora,thora,desloc,opcao):
    desloc= desloc*0.51 +desloc
    total=vhora*thora+desloc 
    total1=total*0.06 
    total2=total - total1
    print("=-=-"*20)
    print(f"Nome do Funcionario : {nome}") 
    print(f"Total de deslocamento :  {desloc}") 
    print(f"valor da hora :{vhora}")
    print (f"total salario bruto : {total}")
    print(f"Total de desconto 6 %  {total1}:") 
    print (f"total salario liquido : {total2}")         

def op3(nome, vhora,thora,desloc,opcao):
    desloc= desloc*0.51 + desloc 
    total=vhora*thora+desloc 
    total1=total*0.05 
    total2=total-total1
    total3=total*0.08 
    total4=total+total3
    print("=-=-"*20)
    print(f"Nome do Funcionario : {nome} ")
    print(f"Total de deslocamento :  {desloc}") 
    print(f"valor da hora :{vhora}")
    print (f"total salario   : {total}")
    print (f"Total adicional periculosidade 8%  {total3}")
    print (f"total salario bruto com adic periculosidade : {total4}") 
    print(f"Total de desconto INSS 5% {total1}:")    
    print (f"total salario liquido com adicional de periculosidade : {total2+total3:.2f}")  

 

nome= str(input("Digite o nome do funcionario :  "))
vhora=float(input("Digite o valor da hora :  ")) 
thora=float (input("Digite a quantidade de hora trabalhada :  ")) 
desloc=float(input("Digite a quantidade de km deslocado :  ")) 
opcao= int (input("Digite '1' para pessoa juridica, '2' - pessoa fisica, e '3' para funcionario CLT :  ")) 
if opcao== 1:
    op1(nome, vhora,thora,desloc,opcao)
elif opcao ==2:
    op2(nome, vhora,thora,desloc,opcao) 
elif opcao ==3: 
    op3(nome, vhora,thora,desloc,opcao) 
