n=int(input("Enter A Year : "))
if n%400==0:
    print("Leap Year")
elif n%4==0 and n%100!=0:
    print("Leap Year")
else:
    print("Not A Leap Year")