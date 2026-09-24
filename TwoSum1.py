class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for i in range(len(nums)):
            if target - nums[i] in sums:
                return [i, sums[target - nums[i]]]
            else:
                sums[nums[i]] = i
        