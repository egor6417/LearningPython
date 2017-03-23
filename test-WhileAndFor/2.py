n=int(input())
sum=0
x=0
for i in range(0,n):
    x=int(input())
    if x%6==0:
        sum=x+sum
    else:
        x=x
print (sum)
        
