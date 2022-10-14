

def mdci(a,b):
    if a < b :
        a,b = b,a

    r = a % b
    while r != 0 :
        a=b
        b=r
        r = a % b
    return b


a=10
b= 15
result=mdci (a,b)
print (f" O mdc de {a,b} é  :{result}")
        
