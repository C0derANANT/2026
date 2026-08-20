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
n=int(input("Enter A Number : "))
print("Prime numbers up to",n,"are:",allprime(n))