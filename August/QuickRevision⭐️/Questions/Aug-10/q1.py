# Strong Password
password = input("Enter password: ")

is_long_enough = len(password) >= 8
first_not_last = password[0] != password[-1]
has_digit = "0" in password or "1" in password or "2" in password or "3" in password or "4" in password or "5" in password or "6" in password or "7" in password or "8" in password or "9" in password

if is_long_enough and first_not_last and has_digit:
    print("Strong")
else:
    print("Weak")