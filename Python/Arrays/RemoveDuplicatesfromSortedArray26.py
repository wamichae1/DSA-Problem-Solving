class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        sSet = set()
        sList = []
        for n in nums:
            if n not in sSet:
                sSet.add(n)
                sList.append(n)
        
        for i in range(len(sList)):
            nums[i] = sList[i]
        
        return len(sList)