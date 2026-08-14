n=(input("Enter A Four Digit Number : "))
odd='13579'
even='24680'
if len(n)==4 and n[0] in even and n[-1] in odd and (int(n[0])+int(n[-1])>int(n[1])+int(n[2])):
    print("PASS")
else:
    print("Fail")
