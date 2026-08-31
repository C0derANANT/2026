n1 = int(input("Enter Number 1: "))
n2 = int(input("Enter Number 2: "))

# Checking the signs
if n1 > 0 and n2 > 0:
    print("Both Numbers Are Positive")

elif n1 < 0 and n2 < 0:
    print("Both Numbers Are Negative")

elif n1 == 0 or n2 == 0:
    print("At Least One Number Is Zero")

else:
    print("One Number Is Positive And One Number Is Negative")


# Finding the greater number
if n1 > n2:
    print(f"{n1} is greater")

elif n2 > n1:
    print(f"{n2} is greater")

else:
    print("Both Are Equal")