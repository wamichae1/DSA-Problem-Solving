class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = set()

        for i, num in enumerate(nums):
            if num in seen:
                return True

            seen.add(num)
            if len(seen) > k:
                seen.remove(nums[i-k]) #since set is unordered, i-k will remove the first element and move the l-pointer
        return False

#slightly faster, since only need to add dict, don't need to remove like in the set solution
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = {}

        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <=k:
                return True
            
            seen[num] = i
            
        return False
