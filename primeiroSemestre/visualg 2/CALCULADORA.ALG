Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Elabore uma calculadora com as quatro operações básicas
//(+, -, *, /). O algoritmo deve solicitar a entrada de dois números e a
//operação a ser executada, na forma de um menu. Dependendo da opção escolhida,
// deve ser executada a operação solicitada e exibido seu resultado. Utilize
//uma variável caractere para armazenar a operação e utilize a estrutura de
// múltipla escolha para selecionar o operador. Perguntar ao usuário se ele
//deseja continuar executando as operações.
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 08/11/2021
Var
// Seção de Declarações das variáveis 
num1,num2,calc, soma:real
continua, opcao:caractere
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

continua <- "sim"

enquanto continua = "sim" faca

escreval ("DIGITE UM NUMERO: ")
leia (num1)
escreval("DIGITE A OPÇÃO : +, -, *, / ")
leia (opcao)
escreval ("DIGITE OUTRO NUMERO: ")
leia (num2)

escolha opcao
caso "+"
soma<- num1 + num2
caso "-"
soma<- num1 - num2
caso "*"
soma<- num1 * num2
caso "/"
soma<- num1 / num2
fimescolha

escreval ("total :", soma)
escreval ("QUER CONTINUAR EXECUTANDO DIGITE sim / não :")
leia (continua)

Fimenquanto

Fimalgoritmo