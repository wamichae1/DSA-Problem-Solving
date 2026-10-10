class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = [[]]
        for n in nums:
            temp = []
            for sublist in ans:
                temp.append(sublist + [n])
            ans += temp
        return ans

#recursion
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def backtrack(start, path):

            result.append(path[:]) # add a copy of the path (snapshot)

            for i in range(start, len(nums)):
                
                path.append(nums[i]) # Add nums[i] into the subset

                backtrack(i + 1, path) # Build the subset from the next element

                path.pop() # Exclude the nums[i] from the subset (backtracking)


        result = []
        backtrack(0, [])
        return result
