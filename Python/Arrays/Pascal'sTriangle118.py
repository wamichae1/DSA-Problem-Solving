class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []
        for nrow in range(numRows):
            temp = [1]
            if nrow < 2:
                for i in range(nrow):
                    temp.append(1)
                triangle.append(temp)
            else:
                for i in range(len(triangle[nrow - 1]) - 1):
                    temp.append(triangle[nrow-1][i] + triangle[nrow-1][i + 1])
                temp.append(1)
                triangle.append(temp)
        return triangle