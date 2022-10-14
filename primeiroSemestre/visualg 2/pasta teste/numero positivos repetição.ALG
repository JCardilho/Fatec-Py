Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : elaborar um algoritimo que receba numero enquanto for positivo
// e no final imprima quantos numero foram digitados
//  : Nome do(a) aluno(a)
// Data atual  : 25/10/2021
Var
// Seção de Declarações das variáveis 
       num, cont :inteiro
       

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...

num <- 1

enquanto num>=0 faca

         escreva("DIGITE UM NUMERO: ")
         leia (num)
         escreval("--------------------------------------")
         
         se num >= 0 entao
            cont <- cont + 1
            escreval ("O NUMERO E POSITIVO")
            escreval("--------------------------------------")
            
         senão
              escreval ("O NUMERO É NEGATIVO")
              escreval("--------------------------------------")
         fimse
fimenquanto

escreval("A QUANTIDADE DE NUMEROS POSITIVOS É: ", cont)
Fimalgoritmo




fim