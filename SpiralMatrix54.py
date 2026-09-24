class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #remove rows and cols to shrink the matrix and get values
        ans = []

        while matrix:
            if matrix:
                ans += matrix.pop(0)
            
            if matrix and matrix[0]:
                for row in matrix:
                    ans.append(row.pop())
            
            if matrix:
                ans += matrix.pop()[::-1]
            
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ans.append(row.pop(0))
        
        return ans
