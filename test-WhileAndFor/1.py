sum=0
x=2
while x!=0:
    x=int(input())
    if (10<=abs(x)<100)and(x%8==0):
        sum=x+sum
    else:
        x=x
print (sum)
        
