class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        final_sum=0
        pre_sum=0
        i,j=0,0
        while i<len(arr):
            pre_sum+=arr[j]
            if (j-i)%2==0:
                final_sum+=pre_sum
            j+=1
            if j==len(arr):
                i+=1
                j=i
                pre_sum=0
        return final_sum
    
    """ TC=O(n^2) SC=O(1)
    return the sum of all odd length subarrays of the given array"""