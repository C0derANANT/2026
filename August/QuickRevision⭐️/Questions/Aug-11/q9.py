day=int(input("Enter Your Day : "))
month=input("Enter Month Name : ")
year=int(input("Enter Your Year : "))

months_31=["january","march","may","july",'august',"october","december"]
months_30=["april","june","september","november"]
valid=True


if year<0:
    valid=False
else:
    if year%4==0:
        if year%100==0:
            if year%400==0:
                leap=True
            else:
                leap=False
        else:
            leap=True
    else:
        leap=False
if leap:
    if month=="february":
        if day>29 or day<1:
            valid=False
    else:
        if month in months_31:
            if day>31 or day<1 :
                valid=False
        elif month in months_30:
            if day>30 or day<1:
                valid=False
        else:
            valid=False
else:
    if month=="february":
        if day>28 or day<1:
            valid=False
    else:
        if month in months_31:
            if day>31 or day<1 :
                valid=False
        elif month in months_30:
            if day>30 or day<1:
                valid=False
        else:
            valid=False
if valid:
    print("Valid Date")
else:
    print("Invalid Date")