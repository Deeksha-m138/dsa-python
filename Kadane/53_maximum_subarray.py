class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m=float('-inf')
        current_sum=0
        for i in range(len(nums)):
            current_sum+=nums[i]
            current_sum=max(nums[i],current_sum)
            m=max(m,current_sum)
        return m      
    
    """ TC=O(n) SC=O(1)
    return the maximum sum of a contiguous subarray represented by the array nums"""