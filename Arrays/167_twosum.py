class Solution(object):
    def twoSum(self, numbers, target):
        i,j=0,len(numbers)-1
        while i<j:
            if numbers[j]+numbers[i]>target:
                j-=1
            elif numbers[i]+numbers[j]<target:
                i+=1
            else:
                return i+1,j+1
            
            """ TC=O(n) SC=O(1)
            return the indices of the two numbers such that they add up to a specific target number."""