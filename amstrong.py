n=int(input("enter the number: "))
k=n
m=len(str(n))
res=0
while k>0:
    res+=pow(k%10,m)
    k=k//10

if res==n:
    print(n,"is amsrong")
else:
    print(n,"is not amsrong")
