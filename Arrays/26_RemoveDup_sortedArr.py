i = 0

for j in range(1, len(nums)):
    if nums[j] != nums[i]:
        i += 1
        nums[i] = nums[j]

print(i + 1)
"""" TC=O(n) SC=O(1) 
nums=list(map(int,input().split()))
candidate=nums[0]
j,i=1,0
while j<len(nums):
  if candidate!=nums[j]:
    candidate=nums[j]
    i+=1
    nums[i]=nums[j]
  j+=1
print(i+1)
"""