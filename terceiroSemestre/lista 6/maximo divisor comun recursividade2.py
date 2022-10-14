def mdc(a,b,c):
    if a < b :
        a,b = b,a

    if a < b:
        return mdc(b,a)
    if b == 0:
        return a
    r= a %b
    return mdc (b,r)


a=10
b= 15
result=mdc(a,b,c)
print (f" O mdc de {a,b} é  :{result}")
        
