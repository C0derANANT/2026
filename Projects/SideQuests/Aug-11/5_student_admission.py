age=int(input("Enter Age: "))
class_12=float(input("Enter Class 12th Percentage: "))
score=float(input("Enter Any Entrance Exam Score: "))
maths_percentage=float(input("Enter Maths Percentage: "))

if age>=18 and class_12>=60 and score>=70 and maths_percentage>=55:
    print("You are eligible for admission.")
else:
    print("You are not eligible for admission.")
