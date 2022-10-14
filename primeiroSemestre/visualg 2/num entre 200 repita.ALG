Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Ler vários números e informar quantos números entre 100 e 200
//foram digitados. Quando o valor 0 (zero) for lido, o algoritmo encerra.//Ler vários números e informar quantos números entre 100 e 200
//foram digitados. Quando o valor 0 (zero) for lido, o algoritmo encerra.
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 19/11/2021
Var
// Seção de Declarações das variáveis 

 num : real
 cont : inteiro
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
cont <- 0
repita
      escreval ("DIGITE UM NUMERO")
      leia (num)
      se (num>=100)e (num <=200)entao
      cont <- cont+1
      fimse
ate num = 0
 escreval("Foram digitados ",Cont," números entre 100 e 200!")
Fimalgoritmo