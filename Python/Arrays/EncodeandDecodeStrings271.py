#neetcode
class Solution:
    #Encode by doing len(s) # s for each str in strs
    def encode(self, strs: List[str]) -> str:
        ans = ""
        for string in strs:
            ans +=  f'{len(string)}#{string}'
        return ans
    
    def decode(self, s: str) -> List[str]:
        ans = []
        p = 0
        while p < len(s):
            num = ""
            while p < len(s) and s[p].isdigit():
                num += s[p]
                p += 1
            num = int(num)

            p += 1
            temp = ""
            for _ in range(num):
                temp += s[p]
                p += 1
            ans.append(temp)
            #use and.append(s[p:p+num]) and p += num to replace this last section in a few lines.
        return ans
