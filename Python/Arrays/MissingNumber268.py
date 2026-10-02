class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #add all the numbers in the list and subtract it from the sum of the length
        return sum(range(len(nums)+1)) - sum(nums)
        