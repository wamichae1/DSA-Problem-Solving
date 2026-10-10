class NumArray:
    #use prefix sum for fast lookup
    def __init__(self, nums: list[int]):
        self.snum = [0]

        for num in nums:
            self.snum.append(self.snum[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.snum[right + 1] - self.snum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)