class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def divisor_sum(nums,div):
            s=0
            for i in range(len(nums)):
                s+=ceil(nums[i]/div)
            return s
        low,high=1,max(nums)
        while low<=high:
            mid=(low+high)//2
            div_sum=divisor_sum(nums,mid)
            if div_sum>threshold:
                low=mid+1
            else:
                high=mid-1
        return low
""" TC=O(nlogm) SC=O(1)  """