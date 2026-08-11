n=input("Enter UserName : ")
if 5<=len(n)<=12 and n[0].isalpha() and n[-1].isdigit() and " " not in n:
    print("Valid Username")
else:
    print("Invalid Username")