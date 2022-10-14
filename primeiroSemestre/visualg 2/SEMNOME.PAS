{ATENÇÃO: Esta rotina ainda está em desenvolvimento.
          O código gerado pode apresentar incorreções sintáticas. }
program semnome;
uses Crt;
// { Disciplina   : [Linguagem e Lógica de Programação]}
// { Professor   : Antonio Carlos Nicolodi}
// { Descrição   : Ler vários números e informar quantos números entre 100 e 200}
// {foram digitados. Quando o valor 0 (zero) for lido, o algoritmo encerra.//Ler vários números and informar}
quantos números entre 100 and 200;
// {foram digitados. Quando o valor 0 (zero) for lido, o algoritmo encerra.}
// { Autor(a)    : Nome do(a) aluno(a)}
// { Data atual  : 19/11/2021}
Var
// { Seção de Declarações das variáveis}

num : real;
cont : integer;
begin
   // { Seção de Comandos, procedimento, funções, operadores, etc...}

   cont := 0;

   repeat
      write('Digite um numero: ');
      readln(num);
      if (num > 100) and (num < 200) then begin
      cont := cont+1;
      end;
   until num = 0;

   writeln('----------------------------------------------');
   writeln('A quantidade de numeros enttre 100 e 200 é:',cont);
end.