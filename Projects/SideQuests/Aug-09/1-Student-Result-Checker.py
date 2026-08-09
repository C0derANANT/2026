name = input("Enter The Name : ")
marks1 = int(input("Enter Marks Of First Subject : "))
marks2 = int(input("Enter Marks Of Second Subject : "))
marks3 = int(input("Enter Marks Of Third Subject : "))

total = marks1 + marks2 + marks3
percentage = total / 3
print(f"Percentage : {percentage:.2f}%")

if marks1 >= 33 and marks2 >= 33 and marks3 >= 33:

    if percentage > 85:
        grade = "A+"
    elif percentage > 70:
        grade = "B"
    elif percentage > 60:
        grade = "C"
    else:
        grade = "D"

    print(f"{name} You Scored Grade {grade}")

else:
    print(f"{name} You Failed")