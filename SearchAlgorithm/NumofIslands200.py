class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #bfs queue
        def bfs(row, col, grid):
            frontier = deque([(row,col)])
            rows = len(grid)
            cols = len(grid[0])
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            while frontier:
                row, col = frontier.popleft()

                for dr,dc in directions:
                    new_row, new_col = dr + row, dc + col
                    if new_row >= 0 and new_row < rows and new_col >= 0 and new_col < cols and grid[new_row][new_col] == "1":
                        grid[new_row][new_col] = "X"
                        frontier.append((new_row, new_col))
        count_island = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    bfs(r, c, grid)
                    count_island += 1
        return count_island
