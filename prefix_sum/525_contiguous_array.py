class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        m=0
        pre_sum=0
        d={0:-1}
        for i in range(len(nums)):
            if nums[i]==0:
                pre_sum-=1
            else:
                pre_sum+=1
            if pre_sum in d:
                m=max(m,i-d[pre_sum])
            if pre_sum not in d:
                d[pre_sum]=i
        return m
    
    """ TC=O(n) SC=O(n)
    return the maximum length of a contiguous subarray with equal number of 0 and 1"""