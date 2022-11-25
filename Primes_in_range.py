import math
def isPrime(x):
    if(x==1):
        return False
    for j in range(2,int(math.sqrt(x)+1)):
        if(x%j==0):
           return False
    return True
m=int(input())
n=int(input())
c=0
for i in range(m,n+1):
  if(isPrime(i)):
     c+=1
print(c)
pg n0:2 numbers 3Q