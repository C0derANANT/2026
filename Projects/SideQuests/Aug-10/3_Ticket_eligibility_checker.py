n=int(input("Enter Your Age : "))
ticket=input("Do You Have A Ticket[Yes/No] : ").lower()

if n>=18 and ticket=='yes':
    print("Eligible")
else:
    print("NOT Eligible")
