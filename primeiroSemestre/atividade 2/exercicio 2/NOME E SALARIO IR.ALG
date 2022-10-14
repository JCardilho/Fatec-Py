Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   :
// Descrição   :
// Autor(a)    :
// Data atual  :
Var
// Seção de Declarações das variáveis 
 nome:caractere
 salario,aliquota:real
 cont:inteiro
 

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
cont<-0
salario<-0
aliquota<-0
para cont de 0 ate 4 faca
     escreval ("DIGITE SEU NOME")
     leia(nome)
     escreval("DIGITE O SÁLARIO BRUTO")
     leia (salario)

     escreval ("NOME:", nome)
     
     se salario <600 entao
     escreval("ISENTO")
     senao
          se salario  < 1500 entao
          aliquota<- (salario *0.10)
          senao
               aliquota<- (salario *0.15)
          fimse
          escreval ("VALOR ALIQUOTA DO IMPOSTO DE RENDA É: ",aliquota)
          fimse
          fimse

fimpara
Fimalgoritmo