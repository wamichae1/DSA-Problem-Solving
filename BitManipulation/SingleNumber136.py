class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #xor returns 0 if both bits are the same, 1 if not
        #Finds duplicate here
        r = 0
        for num in nums:
            r ^= num
        return r

