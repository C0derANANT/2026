# Voting
n=int(input("Enter your age: "))
if n>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


# Grades
marks=int(input("Enter your marks: "))
if marks<=100 and marks>=0:
    if marks>=90:
        print("A Grade")
    elif marks>=80:
        print("B Grade")
    elif marks>=70:
        print("C Grade")
    elif marks>=60:
        print("D Grade")
    else:
        print("F Grade")
else:
    print("Invalid Marks")