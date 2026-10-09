class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0]*(n+1)
        prev = 1
        for i in range(1, n + 1):
            if 2*prev == i:
                prev = i
            ans[i] = 1 + ans[i-prev]
            
        return ans