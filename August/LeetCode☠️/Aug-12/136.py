nums = [4,1,2,1,2]
s1=set(nums)
for i in s1:
    if nums.count(i)==1:
        print(i)