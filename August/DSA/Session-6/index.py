# Binary Number System
# Decimal To Binary
binary = ''
n = int(input("Enter A Decimal Number: "))

if n == 0:
    print("0")
else:
    while n > 0:
        binary += str(n % 2)
        n = n // 2

    print(binary[::-1])

# Binary To Decimal
n=int(input("Enter A Binary Number : "))
power=0
decimal=0
while n>0:
    decimal+=(n%10)*2**(power)
    power+=1
    n=n//10
print(decimal)