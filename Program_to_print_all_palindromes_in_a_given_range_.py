def isPalindrome(x):
    l=0
    temp=x
    while(x>0):
        r=x%10
        l=l*10+r
        x//=10
    if(temp==l):
      return True
    return False
m=int(input())
n=int(input())
for i in range(m,n+1):
  if(isPalindrome(i)):
      print(i,end=" ")
      
      
      program to print palindrome