# Build a three-number mathematical analyzer.
# Input: number1, number2, number3.
# Determine:
# • Largest number
# • Smallest number
# • Whether all three are equal
# • Whether exactly two are equal
# • Whether all three are different
# • Whether the largest is even or odd
# • Whether the smallest is positive, negative, or zero
# • Whether the sum of all three is positive, negative, or zero
# Restriction: Do this using only concepts you have already studied. No lists, loops, functions, or
# unlearned shortcuts.
n1=int(input("Enter First Number : "))
n2=int(input("Enter Second Number : "))
n3=int(input("Enter Third Number : "))
if n1>n2 and n1>n3:
    largest=n1  
elif n2>n3:
    largest=n2
else:
    largest=n3

if n1<n2 and n1<n3:
    smallest=n1
elif n2<n3:
    smallest=n2
else:
    smallest=n3


if n1==n2==n3:
    print("All Three Numbers are Equal")
elif n1==n2 or n2==n3 or n1==n3:
    print("Exactly Two Numbers are Equal")
else:
    print("All Three Numbers are Different")     

if largest%2==0:
    print("Largest Number is Even")
else:
    print("Largest Number is Odd")


if smallest>0:
    print("Smallest Number is Positive")
elif smallest<0:
    print("Smallest Number is Negative")
else:
    print("Smallest Number is Zero")


if n1+n2+n3>0:
    print("Sum of All Three Numbers is Positive")
elif n1+n2+n3<0:
    print("Sum of All Three Numbers is Negative")
else:   
    print("Sum of All Three Numbers is Zero")