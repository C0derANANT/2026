# Reversing An Array
# 2-pointer Approach
arr=[4,2,7,8,1]
left=0
right=len(arr)-1

while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1
