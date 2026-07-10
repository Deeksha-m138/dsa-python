class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles)==h:
            return max(piles)
        def hours_taken(piles,bananas):
            total_hr=0
            for i in range(len(piles)):
                total_hr+=ceil(piles[i]/bananas)
            return total_hr
        low,high=1,max(piles)
        while low<=high:
            mid=(low+high)//2
            total_hrs=hours_taken(piles,mid)
            if total_hrs<=h:
                high=mid-1
            else:
                low=mid+1
        return low

""" TC=O(nlogm) SC=O(1)  """