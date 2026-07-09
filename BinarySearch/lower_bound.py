nums=list(map(int,input().split()))
low,high=0,len(nums)-1
while low<=high:
    mid=(high+low)//2
    if nums[mid]==target or nums[mid]>target:
        high=mid-1
    else:
        low=mid+1
print(low)

""" TC=O(logn) SC=O(1) """