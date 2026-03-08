n = int(input("Enter decimal number: "))
print(bin(n)[2:]) 
k = n
binary = ""

while k > 0:
    remainder = k % 2
    binary = str(remainder) + binary   
    k = k // 2

print(n, "in binary is", binary)
