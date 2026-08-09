distance=float(input("Enter The Distance Travelled (In Kms) : "))
time=float(input("Enter The Time Taken For Travel (In Hrs) : "))
speed=distance/time
if speed >= 100:
    print(f"{speed}kmph : Fast Speed")
elif speed>=60:
    print(f"{speed}kmph : Moderate Speed")
else:
    print(f"{speed}kmph : Slow Speed")