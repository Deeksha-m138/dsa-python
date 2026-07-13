class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i-1]==nums[i]:
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                n=[]
                s=nums[i]+nums[j]+nums[k]
                if s>0:
                    k-=1
                elif s<0:
                    j+=1
                else:
                    n=[nums[i],nums[j],nums[k]]
                    ans.append(n)
                    while j<k and nums[j]==nums[j+1]:
                        j+=1
                    while j<k and nums[k]==nums[k-1]:
                        k-=1
                    k-=1
                    j+=1
        return ans
        """ TC=O(n^2) SC=O(n)  """