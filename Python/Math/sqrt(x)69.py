class Solution:
    def mySqrt(self, x: int) -> int:

        if x < 2:
            return x
        l = 1
        r = x

        while l <= r:
            mid = (l + r) // 2
            if x // mid ==  mid:
                return mid
            if x // mid > mid:
                l = mid + 1
            else:
                r = mid - 1
        return r #largest possible valid int
        