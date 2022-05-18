#program to print n fibonacci numbers
n=int(input("enter value n"))
print("fibonacci numbers are")
if n==1:
    print(1)
elif n==2:
    print("0,1")
else:
    n1=0
    n2=1
    i=1
    fib=0
    print(0)
    print(1)
    while i<=n:
        
        fib=n1+n2
        print(fib)
        n1=n2
        n2=fib
        i=i+1