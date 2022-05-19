#write a python program to print all positive numbers in a range
n1=int(input("enter stating value of your range"))
n2=int(input("enter ending value of your range")) 
rag=range(n1,n2+1) 
i=n1
for i in rag:
    if i>0:
        print(i)
    i=i+1    
  