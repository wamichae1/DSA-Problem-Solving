class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        new = []
        for i in range(len(nums)):
            if nums[i] == target:
                new.append(i)
        return new