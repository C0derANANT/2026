n=input("Enter A Code : ")
numbers='1234567890'
if len(n)==7 and  n[3] != n[5] or ( n[0] in numbers
    or n[1] in numbers or n[2] in numbers
    or n[4] in numbers or n[5] in numbers
    or n[6] in numbers ) and "BAD" not in n:
    print("Valid Code")
else:
    print("Invalid Code")
