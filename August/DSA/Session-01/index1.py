# Sum Of Numbers Upto N
n=int(input("Enter a number: "))
sum=0
for i in range(1,n+1):
    sum+=i
print("Sum of numbers upto", n, "is:", sum)

# Prime Number Check
a=int(input("Enter a number: "))
if a>1:
    for i in range(2,a):
        if a%i==0:
            print(a, "is not a prime number.")
            break
    else:
        print(a, "is a prime number.")