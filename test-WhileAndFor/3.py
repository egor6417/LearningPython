n=int(input())
sum=0
x=0
b=0
z=0
max=1
for i in range(0,n):
    x=int(input())
    if x>max:
        max=x
    if x==0:
        z=1

print (max)    
for i in range(0,n):
    b=(x)
    if z==0:
        print("N0")
    else:
        print("YES")
        
