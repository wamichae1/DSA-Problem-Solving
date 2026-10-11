class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backtrack(path):
            if len(path) == len(nums):
                result.append(path[:])
    
            for n in nums:
                if n in path:
                    continue

                path.append(n)
                backtrack(path)
                path.pop()
        
        result = []
        backtrack([])
        return result

#visited set
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backtrack(path, visited):
            if len(path) == len(nums):
                result.append(path[:])
    
            for n in nums:
                if n in visited:
                    continue

                path.append(n)
                visited.add(n)
                backtrack(path, visited)
                popped = path.pop()
                visited.remove(n)
        
        result = []
        backtrack([], set())
        return result

