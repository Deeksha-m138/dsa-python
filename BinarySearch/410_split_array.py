class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(nums,k,l):
            s,sub_array=0,1
            for num in nums:
                if s+num<=l:
                    s+=num
                else:
                    sub_array+=1
                    s=num
            return sub_array
        low,high=max(nums),sum(nums)
        while low<=high:
            mid=(low+high)//2
            sub_array=check(nums,k,mid)
            if sub_array<=k:
                high=mid-1
            else:
                low=mid+1
        return low
"" "TC=O(nlogn) SC=O(1)  """