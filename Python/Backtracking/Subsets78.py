class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = [[]]
        for n in nums:
            temp = []
            for sublist in ans:
                temp.append(sublist + [n])
            ans += temp
        return ans

