class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        final = []
        nums.sort()
        for p1 in range(len(nums) - 2):
            if p1 > 0 and nums[p1] == nums[p1-1]:
                continue
            p2, p3 = p1+ 1, len(nums) - 1
            while p2<p3:
                threesum = nums[p1] + nums[p2] + nums[p3]
                if threesum == 0:
                    final.append((nums[p1],nums[p2],nums[p3]))
                    p2 += 1
                    p3 -= 1
                    while p2 < p3 and nums[p2] == nums[p2 - 1]:
                        p2 += 1
                    while p3 > p2 and nums[p3] == nums[p3 + 1]:
                        p3 -= 1                    
                elif threesum > 0:
                    p3 -= 1
                else:
                    p2 += 1
        return final
        