class Solution:
    def trap(self, height: list[int]) -> int:
        maxLeft = height[0]
        maxRight = height[-1] 
        l = 0
        r = len(height) - 1
        water = 0
        while l < r:
            if height[l] <= height[r]:
                if maxLeft <= height[l]: 
                    maxLeft = height[l]
                else: #if l < r and l < maxLeft
                    water += maxLeft - height[l]
                l += 1
            else:
                if maxRight <= height[r]:
                    maxRight = height[r]
                else: # if r < l and r < maxRight
                    water += maxRight - height[r]
                r -= 1
        return water



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