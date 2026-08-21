# Q1-Calculate Simple Interest (SI) using the Basic formula:
P=int(input("Enter the principal amount (P): "))
R=float(input("Enter the rate of interest (R) in percentage: "))
T=float(input("Enter the time (T) in years: "))
SI = (P * R * T) / 100
print("Simple Interest (SI):", SI)

# Q2-Calculate Max Of Two Numbers
n1=int(input("Enter First Number : "))
n2=int(input("Enter Second Number : "))
if n1>n2:
    print(f"{n2} Is Greater")
else:
    print(f"{n1} Is Greater")

# Q3-Calculate the factorial of n
n=int(input("Enter A Number: "))
factorial=1
for i in range(n):
    factorial*=i+1
print(f'Factorial of {n} is : {factorial}')

# Q4-Valid Driving License
age=int(input("Enter Your Age: "))
if age>=18:
    print("You are eligible for a driving license.")
else:
    print("You are not eligible for a driving license.")