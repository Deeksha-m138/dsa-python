class Solution:
    def mySqrt(self, x: int) -> int:
        low,high=1,x
        while low<=high:
            mid=(high+low)//2
            if mid*mid==x:
                return mid
            if mid*mid>x:
                high=mid-1
            else:
                low=mid+1
        return high
    
    """ TC=O(logn) SC=O(1)  """         