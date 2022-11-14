# generate fibonacci number 
n=int(input('enter number of fibonacci number you want ->'))
a=0
b=1
print(a,b,end=' ')
for i in range(n-2):
    c=a+b
    print(c,end=' ')
    a=b
    b=c