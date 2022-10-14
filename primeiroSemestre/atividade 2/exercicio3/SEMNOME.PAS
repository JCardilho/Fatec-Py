{ATENÇÃO: Esta rotina ainda está em desenvolvimento.
          O código gerado pode apresentar incorreções sintáticas. }
program semnome;
uses Crt;
// { Disciplina   : [Linguagem e Lógica de Programação]}
// { Professor   :}
// { Descrição   : Aqui você descreve o que o programa faz! (função)}
// { Autor(a)    : Nome do(a) aluno(a)}
// { Data atual  : 17/09/2021}

var
numero, par, impar,cont: integer;

begin
   par:= 0;
   impar:= 0;
   cont:=0;
   repeat
      write('Informe um NUMERO: ');
      readln(numero);
      cont:= cont+1;
      if numero mod2 = 0 then begin
      par:= par+1;
      end else begin
      impar:= impar+1;
      end;
   until cont =8;
   writeln ('TOTAL DE NUMEROS PAR:', par);
   writeln ('TOTAL DE NUMEROS PAR:', impar);


end.