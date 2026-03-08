def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a+b
        
        
n=int(input("enter the number up siries: "))


if n<=0:
    print("Enter a positive number")
else:
    fibonacci(n)
