class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x=""
        for i in range(len(digits)):
            x+=str(digits[i])
        n=int(x)+1
        nums=list(map(int,str(n)))
        return nums
""" TC=O(n) SC=O(n)  """