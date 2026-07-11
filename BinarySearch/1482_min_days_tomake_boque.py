class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):
            return -1
        def check(bloomDay,day,k):
            m,flower=0,0
            for i in range(len(bloomDay)):
                if day>=bloomDay[i]:
                    flower+=1
                    if flower==k:
                        m+=1
                        flower=0
                else:
                    flower=0
            return m
        low,high=min(bloomDay),max(bloomDay)
        while low<=high:
            mid=(low+high)//2
            bouquets=check(bloomDay,mid,k)
            if bouquets<m:
                low=mid+1
            else:
                high=mid-1
        return low 
        
        """ TC=O(nlogm) SC=O(1)  """