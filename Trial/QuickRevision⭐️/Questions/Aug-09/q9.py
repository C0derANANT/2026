a = int(input("First number: "))
b = int(input("Second number: "))
print(f'Before Swap: a={a}, b={b}')
a, b = b, a
print(f"After Swap: a={a}, b={b}")