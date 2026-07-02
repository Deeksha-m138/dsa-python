class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        def generate_row(row):
            result=[]
            res=1
            result.append(res)
            for col in range(1,row):
                res=res*(row-col)
                res=res//col
                result.append(res)
            return result
        for i in range(1,numRows+1):
            ans.append(generate_row(i))
        return ans
        
        """ TC=O(n^2) SC=O(1)
        return the pascal triangle of n rows"""