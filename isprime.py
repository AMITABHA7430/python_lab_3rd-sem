n = int(input("Enter the number: "))

if n<2:
    print(n,"is a prime number")
    
else:
    isprime = True;
    for i in range (2,int(n**0.5)+1):
        if n % i==0:
            isprime = False

if isprime:
    print(n,"is a prime number")
    
else:
    print(n,"is not a prime number")
