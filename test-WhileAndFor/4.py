x=int(input())
sum=0
while x>0:
    b=x%10
    if (b>2)and(b<8):
        sum=sum+1
    x=(x-b)/10
print (sum)
        
