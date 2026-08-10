# Greatest Among Three Numbers
n1=int(input("Enter A Number : "))
n2=int(input("Enter A Number : "))
n3=int(input("Enter A Number : "))
if n1>=n2 and n1>=n3:
    print(f"{n1} Is The Largest")
elif n2>=n3 and n2>=n1:
    print(f"{n2} Is The Largest")
elif n3>=n1 and n3>=n2 :
    print(f"{n3} Is The Largest")

# Mulitple Of 7
n=int(input("Enter A Number:"))
if n%7==0:
    print(f'{n} Is A Multiple Of 7')
else:
    print(f'{n} NOT Is A Multiple Of 7')
