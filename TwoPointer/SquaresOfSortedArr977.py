class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        ans = []
        l, r = 0, len(nums) - 1

        while l <= r:
            sqrl = nums[l]**2
            sqrr = nums[r]**2
            if sqrl >= sqrr:
                ans.append(sqrl)
                l += 1
            else:
                ans.append(sqrr)
                r -= 1
        return ans[::-1]

