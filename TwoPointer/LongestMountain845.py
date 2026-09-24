class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        mount = 0
        if len(arr) == 1:
            return mount
        r = 0
        l = 0
        inc = False
        dec = False
        while l < len(arr):
            if r + 1 < len(arr) and arr[r + 1] > arr[r] and not dec:
                r += 1
                inc = True
            else:
                if inc:
                    if r + 1 < len(arr) and arr[r+1] < arr[r]:
                        r += 1
                        dec = True
                    else:
                        if inc and dec:
                            
                            mount = max(mount, r - l + 1)
                        l = r
                        inc, dec  = False, False
                elif not inc:
                    if l == r and l < len(arr):
                        l += 1
                        r = l
                    else:
                        l = r
                    inc, dec = False, False
        return mount


