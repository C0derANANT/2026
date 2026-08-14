n=input("Enter A String : ")
if n[0].isupper() and n[-1].isdigit() and len(n)>=6:
    print("Matches")
else :
    print("Does not match")