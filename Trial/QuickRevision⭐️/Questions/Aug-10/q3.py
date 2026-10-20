# Email Check

n=input("Enter An E-Mail : ")
ch_before=n.index('@')-1
no_of_ch_after=len(n)-1-n.index("@")
if n.count("@")==1 and ch_before>=0 and no_of_ch_after>0 and n[n.index("@")+1]!=" " : 
    print("Valid")
else:
    print("Invalid")
