n,x=map(int,input().split())
n=str(n)
fn=int(n[:x])
sn=int(n[-x:])
print(abs(fn-sn))
