Algoritmo "semnome"
// Disciplina   : [Linguagem e L?gica de Programa??o]
// Professor   : Antonio Carlos Nicolodi 
// Descri??o   : Elabore uma calculadora com as quatro opera??es b?sicas
//(+, -, *, /). O algoritmo deve solicitar a entrada de dois n?meros e a
//opera??o a ser executada, na forma de um menu. Dependendo da op??o escolhida,
// deve ser executada a opera??o solicitada e exibido seu resultado. Utilize
//uma vari?vel caractere para armazenar a opera??o e utilize a estrutura de
// m?ltipla escolha para selecionar o operador. Perguntar ao usu?rio se ele
//deseja continuar executando as opera??es.
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 08/11/2021
Var
// Se??o de Declara??es das vari?veis 
num1,num2,calc, soma:real
continua, opcao:caractere
Inicio
// Se??o de Comandos, procedimento, fun??es, operadores, etc... 

continua <- "sim"

enquanto continua = "sim" faca

escreval ("DIGITE UM NUMERO: ")
leia (num1)
escreval("DIGITE A OP??O : +, -, *, / ")
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
escreval ("QUER CONTINUAR EXECUTANDO DIGITE sim / n?o :")
leia (continua)

Fimenquanto

Fimalgoritmo