class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        sorted_nums = sorted(nums)

        d = {}

        for i, num in enumerate(sorted_nums):
            if num not in d:
                d[num] = i
        #list comprehension dict value for every num in nums
        return [d[num] for num in nums]