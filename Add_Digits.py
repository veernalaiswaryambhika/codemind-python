n=int(input())
t=n
while True:
    s=0
    while(n!=0):
        r=n%10
        s=s+r
        n//=10
    if s<10:
        print(s)
        break
    else:
        n=s