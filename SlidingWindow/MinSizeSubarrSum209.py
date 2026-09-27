class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        count = 0
        window = 0
        ans = float("inf")
        l = 0
        for r in range(len(nums)):
            window += 1
            count += nums[r]
            if count >= target:
                ans = min(ans, window)
                while l + 1 < len(nums) and l <= r:
                    
                    if window > 1:
                        window -= 1
                        count -= nums[l]
                        l += 1
                    else:
                        l += 1

                    if count >= target:
                        ans = min(ans, window)
                    elif count < target:
                        break

        if ans == float("inf"):
            return 0
        else:
            return ans
#Efficient solution
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        count = 0
        ans = float("inf")
        l = 0
        for r in range(len(nums)):
            count += nums[r]

            while count >= target:
                ans = min(ans, r - l + 1) #calculate window directly using pointers
                count -= nums[l]
                l += 1
        return 0 if ans == float("inf") else ans