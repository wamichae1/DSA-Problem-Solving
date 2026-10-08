class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):

            dp[i] = max(nums[i], nums[i] + dp[i-1])
        
        return max(dp)



class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = nums[0]
        currentSum = 0

        for n in nums:
            if currentSum < 0:
                currentSum = 0

            currentSum += n
            maxSum = max(maxSum, currentSum)
        return maxSum

        
        