a=int(input("Enter Length Of First Side : "))
b=int(input("Enter Length Of Second Side : "))
c=int(input("Enter Length Of Third Side : "))

if a>0 and b>0 and c>0:
    if a+b>c and b+c>a and c+a>b:
        print("Valid Triangle")

        if a==b==c:
            print("Equilateral Triangle")
        elif a!=b and b!=c and c!=a:
            print("Scalene Triangle")
        else:
            print("Isosceles Triangle")
    else:
        print("Invalid Triangle")
else:
    print("Invalid, Negative Sides")