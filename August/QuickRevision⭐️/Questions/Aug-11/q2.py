age=int(input("Enter Your Age : "))
p=float(input("Enter Your Percentage : "))
z=f'''
Age : {age}
Percentage : {p}
'''
if age<0 or p<0:
    print("Invalid")
else:
    if age>=18:
        if p>=60:
            print(z)
            print("\nEligible")
        else:
            print(z)
            print("\nPercentage Requirement Failed")
    else:
        if p>=60:
            print(z)
            print("\nAge Requirement Failed")
        else:
            print(z)
            print("\nBoth Requirement Failed")
