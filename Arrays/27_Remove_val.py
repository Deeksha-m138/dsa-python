nums=list(map(int,input().split()))
val=int(input())
i=0
for j in range(len(nums)):
  if val!=nums[j]:
    nums[i]=nums[j]
    i+=1
print(i)
""" TC=O(n) SC=O(1)
modify in place and return the new length of the array after removing all instances of val. 
The order of elements can be changed, and it doesn't matter what you leave beyond the new length."""