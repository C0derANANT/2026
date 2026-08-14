# Palindrome Check
palindrome=input("Enter Phrase : ")
palindrome=palindrome.replace(" ",'').lower()
rev=palindrome[::-1]

if rev==palindrome:
    print("Palindrome")
else :
    print("NOT a Palindrome")