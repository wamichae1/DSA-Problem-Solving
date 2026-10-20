#Multiple Passes 3x81 ops
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for row in range(len(board)):
            temp = set()
            for col in range(len(board[0])):
                if board[row][col] != ".":
                    if board[row][col] in temp:
                        return False
                    else:
                        temp.add(board[row][col])

        for col in range(9):
            temp = set()
            for row in range(9):
                if board[row][col] != ".":
                    if board[row][col] in temp:
                        return False
                    else:
                        temp.add(board[row][col])
        sqr = [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]

        for r,c in sqr:
            temp = set()
            for i in range(3):
                for j in range(3):
                    square = board[r + i][c + j]
                    if square != ".":
                        if square in temp:
                            return False
                        else:
                            temp.add(square)
        return True
        