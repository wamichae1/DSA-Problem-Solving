class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 0
        ans = 1
        for i in range(n):
            temp = ans
            ans = ans + prev
            prev = temp
        return ans