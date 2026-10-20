n=input("Enter A String : ")
if len(n)>=3:
    print(n[:3])
else:
    print("N/A")
print(n[-2:])
if len(n)>=6:
    print(n[1],n[3],n[5])
else:
    print("N/A")
print(n[::-1])
