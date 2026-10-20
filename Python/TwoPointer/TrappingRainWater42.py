class Solution:
    def trap(self, height: list[int]) -> int:
        mL, mR = 0,0
        l = 0
        r = len(height) - 1

        while l < r:
            


#prefix max list solution, o(n) space
class Solution:
    def trap(self, height: list[int]) -> int:
        water = []
        prel = []
        prer = []
        maxl = 0
        for i in range(len(height)):
            maxl = max(maxl, height[i])
            prel.append(maxl)
        
        maxr = 0
        for i in range(len(height) - 1,  -1, -1):
            maxr = max(maxr, height[i])
            prer.insert(0 ,maxr)

        for i in range(len(height)):
            water.append(min(prel[i], prer[i]) - height[i])

        return sum(water)