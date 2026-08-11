n=input("Enter A Phone Number : ")
numbers='0123456789'
if len(n)==8 and (n[3]=="-" or n[3]==' ') and( n[0] in numbers
    and n[1] in numbers and n[2] in numbers
    and n[4] in numbers and n[5] in numbers
    and n[6] in numbers and n[7] in numbers):
    print("Valid Phone Number ")
else:
    print("Invalid Phone Number")