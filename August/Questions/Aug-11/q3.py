a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
c = int(input("Enter Third Number : "))
if b == a or b == c:
    print("Middle value is equal to at least one other value")
elif b > a and b > c:
    print("Middle value is greater than both")
elif b < a and b < c:
    print("Middle value is smaller than both")
else:
    print("Middle value is between the other two")