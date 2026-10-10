class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        def backtrack(start, path):
            if len(path) == k:
                result.append(path[:])

            for i in range(start, n + 1):
                if len(path) < k:
                    path.append(i)
                    backtrack(i + 1, path)
                    path.pop()

        result = []
        backtrack(1, [])
        return result