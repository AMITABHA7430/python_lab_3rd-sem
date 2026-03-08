n=int(input("enter the number: "))
k=n
res =0
if k<2:
    print(n,"is not a perfect number")
    

for i in range(1,n):
    if k%i==0:
        res+=i
        
        
if res==n:
    print(n,"is a perfect number")
else:
    print(n,"is not a perfect number")
