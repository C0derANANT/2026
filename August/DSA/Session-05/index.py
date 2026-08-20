def square(n):
    return n**2


def cube(n):
    return n**3

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def allprime(n):
    primes = []
    for i in range(2, n + 1):
        if prime(i):
            primes.append(i)
    return primes


# Fibonacci Series
def fibonacci(n):
    a = 0
    b = 1
    c = a + b
    print(0, 1, end=',')
    if n < 0:
        print("Please enter a positive number")
    elif n == 0:
        print("0")
    elif n == 1:
        print("0")
    elif n == 2:
        print("0,1")
    else:
        for i in range(n-2):
            print(c,end=',')
            a=b
            b=c
            c=a+b

n=int(input("Enter A Number : "))
print("Prime numbers up to",n,"are:",allprime(n))
print("Fibonacci series up to",n,"terms is:")
fibonacci(n)
