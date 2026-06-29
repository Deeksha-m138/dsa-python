class Solution(object):
    def moveZeroes(self, nums):
        i=0
        for j in range(len(nums)):
            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1

                """ TC=O(n) SC=O(1)
                modify in place and return the new length of the array after moving all zeroes to the"""
            
