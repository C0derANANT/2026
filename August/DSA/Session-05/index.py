def square(n):
    return n**2


def cube(n):
    return n**3

n=int(input("Enter A Number : "))
print("Square of",n,"is",square(n))
# print("Cube of",n,"is",cube(n))

lambda_square = lambda n: n**2