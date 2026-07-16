class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        m, n = len(matrix), len(matrix[0])
        
        # Start at the top-right corner
        row = 0
        col = n - 1
        
        while row < m and col >= 0:
            current = matrix[row][col]
            
            if current == target:
                return True
            elif current > target:
                col -= 1  # Move left (eliminate column)
            else:
                row += 1  # Move down (eliminate row)
                
        return False
        """TC=O(m+n) SC=O(1)  """