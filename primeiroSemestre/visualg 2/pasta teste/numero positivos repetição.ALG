Algoritmo "semnome"
// Disciplina   : [Linguagem e L?gica de Programa??o]
// Professor   : Antonio Carlos Nicolodi 
// Descri??o   : elaborar um algoritimo que receba numero enquanto for positivo
// e no final imprima quantos numero foram digitados
//  : Nome do(a) aluno(a)
// Data atual  : 25/10/2021
Var
// Se??o de Declara??es das vari?veis 
       num, cont :inteiro
       

Inicio
// Se??o de Comandos, procedimento, fun??es, operadores, etc...

num <- 1

enquanto num>=0 faca

         escreva("DIGITE UM NUMERO: ")
         leia (num)
         escreval("--------------------------------------")
         
         se num >= 0 entao
            cont <- cont + 1
            escreval ("O NUMERO E POSITIVO")
            escreval("--------------------------------------")
            
         sen?o
              escreval ("O NUMERO ? NEGATIVO")
              escreval("--------------------------------------")
         fimse
fimenquanto

escreval("A QUANTIDADE DE NUMEROS POSITIVOS ?: ", cont)
Fimalgoritmo




fim