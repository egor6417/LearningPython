n=int(input())
sum=0
x=0
b=0
max=1
for i in range(0,n):
    x=int(input())
    if x>max:
        max=x
    else:
        x=x

print (max)    
for i in range(0,n):
    b=int(input())
    if (b<30)and(b>1)and(b<300):
        print("YES")
    else:
        print("N0")
        
