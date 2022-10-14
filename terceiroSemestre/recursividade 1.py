def fatorial (num):
    if num ==1:
        return 1
        print (num)

    else:
        print(num)
        res=num * fatorial (num-1)
        return res

num = int (input("digite um numero inteiro"))
res=fatorial (num)
print (res)