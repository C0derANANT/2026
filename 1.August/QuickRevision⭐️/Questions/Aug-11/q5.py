n1=int(input("Enter Marks Of Student 1 : "))
n2=int(input("Enter Marks Of Student 2 : "))
n3=int(input("Enter Marks Of Student 3 : "))
percentage=(n1+n2+n3)/3
if n1>=40 and n2>=40 and n3>=40:
    if percentage>=90:
        print("A")
    elif percentage>=75:
        print("B")
    elif percentage>=60:
        print("C")
    else:
        print("D")
else:
    print("F")   