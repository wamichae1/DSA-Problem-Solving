class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        ans = [""]
        for c in s:
            temp = []
            if c.isalpha():
                for o in ans:
                    temp.append(o + c)
                    temp.append(o + c.swapcase())
            else:
                for o in ans:
                    temp.append(o + c)
            ans = temp
        return ans