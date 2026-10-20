n=input("Enter A String : ")
hello_check=n.lower()
upper_alphabets='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
if 'hello' in hello_check and (
    upper_alphabets[0] in n or upper_alphabets[1] in n or
     upper_alphabets[2] in n or upper_alphabets[3] in n or
     upper_alphabets[4] in n or upper_alphabets[5] in n or
     upper_alphabets[6] in n or upper_alphabets[7] in n or
     upper_alphabets[8] in n or upper_alphabets[9] in n or
     upper_alphabets[10] in n or upper_alphabets[11] in n or
     upper_alphabets[12] in n or upper_alphabets[13] in n or
     upper_alphabets[14] in n or upper_alphabets[15] in n or
     upper_alphabets[16] in n or upper_alphabets[17] in n or
     upper_alphabets[18] in n or upper_alphabets[19] in n or
     upper_alphabets[20] in n or upper_alphabets[21] in n or
     upper_alphabets[22] in n or upper_alphabets[23] in n or
     upper_alphabets[24] in n or upper_alphabets[25] in n) and len(n)>5:
    print("Valid Greeting")
else:
    print("Invalid Greeting")