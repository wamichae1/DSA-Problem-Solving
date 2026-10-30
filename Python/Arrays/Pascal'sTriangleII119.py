class Solution:
    def getRow(self, rowIndex: int) -> list[int]:

        def factorial(n):
            result = 1
            for i in range(2, n + 1):
                result *= i
            return result
        
        def combination(n,r):
            return int(factorial(n)/(factorial(r)*factorial(n-r)))
        
        row = [1]
        for i in range(1, rowIndex):
            row.append(combination(rowIndex, i))
        if rowIndex > 0:
            row.append(1)
        return row



        