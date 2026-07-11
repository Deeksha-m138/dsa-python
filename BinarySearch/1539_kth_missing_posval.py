class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low,high=0,len(arr)-1
        while low<=high:
            mid=(low+high)//2
            ele_missing=arr[mid]-mid-1
            if ele_missing<k:
                low=mid+1
            else:
                high=mid-1
        return arr[high]+(k-(arr[high]-high-1))  """low+k"""

        """ TC=O(logn) SC=O(1)  """