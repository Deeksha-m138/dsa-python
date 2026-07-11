class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def capacity_check(weights,capacity):
            days,w,i=0,0,0
            while i<len(weights):
                w+=weights[i]
                if w==capacity:
                    days+=1
                    w=0
                elif w>capacity:
                    days+=1
                    w=weights[i]
                i+=1
            if w>0:
                days+=1
            return days
        low,high=max(weights),sum(weights)
        while low<=high:
            mid=(low+high)//2
            days_taken=capacity_check(weights,mid)
            if days_taken<=days:
                high=mid-1
            else:
                low=mid+1
        return low
        """ TC=O(nlogm) SC=O(1)  """