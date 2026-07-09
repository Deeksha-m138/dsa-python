nums=list(map(int,input().split()))
target=int(input())
low,high=0,len(nums)-1
while low<=high:
    mid=(high+low)//2
    if nums[mid]>=target:
        high=mid-1
    else:
        low=mid+1
print(nums[low])

""" TC=O(logn) SC=O(1)  """