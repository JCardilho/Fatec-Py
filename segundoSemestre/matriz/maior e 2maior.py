import random
tam= 5
mat= [0]*tam
for i in range(tam):
    mat[i] = [0]*tam
for i in range(tam):
    print(mat[i])
for i in range(tam):
    for j in range(tam):
        mat[i][j] = random.randint(0, 99)
for i in range(tam):
    print(mat[i])

maior = mat[0][0]
for i in range(tam):
    for j in range(tam):
        if mat[i][j] > maior:
            maior = mat[i][j]
print("O maior elemento  ",maior)
segundomaior= 0
for i in range(tam):
    for j in range(tam):
        if mat[i][j] > segundomaior and mat[i][j] != maior:
            segundomaior= mat[i][j]
print("O segundo maior elemento: ",segundomaior)
