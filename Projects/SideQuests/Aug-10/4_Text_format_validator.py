n=input("Enter Your String : ")
if len(n)==8 and n[0].isupper() and n[-1].isdigit() and ' ' not in n :
    print("Valid Format")
else:
    print("Invalid Format")