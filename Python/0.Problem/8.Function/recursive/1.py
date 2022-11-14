# WAP to generate first 15 numbers of fibonacci sequence  
def recursive_fibonacci_number(n):
    '''recursive fibonacci sequence'''
    if n==0 or n==1:
        return n
    else:
        # print(recursive_fibonacci_number(n))
        return recursive_fibonacci_number(n-1)+recursive_fibonacci_number(n-2)

n=int(input('How many fibonacci squence do you want - > '))
for i in range(n):
    print(recursive_fibonacci_number(i),end=' ')
