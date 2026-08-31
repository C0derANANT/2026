age=int(input("Enter Your Age : "))
monthly_income=int(input("Enter Your Monthly Income :"))
credit_score=int(input("Enter Your Credit Score : "))
if age >= 25 and monthly_income >= 50000 and credit_score >=750:
    print("Premium")
elif age >= 21 and monthly_income >= 25000 and credit_score >=650:
    print("Standard")
elif age >= 18 and monthly_income >= 15000 and credit_score >=550:
    print("Basic")
# elif age<0:
#     print("Rejected")
else:
    print("Rejected")