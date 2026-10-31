class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {")":"(", "]":"[", "}":"{"}
        brackets = []
        for c in s:
            if c in parenthesis.values():
                brackets.append(c)
            elif c in parenthesis:
                if not brackets or brackets[-1] != parenthesis[c]:
                    return False
                brackets.pop()
        return not brackets

#2 dict, cleaner logic?

class Solution:
    def isValid(self, s: str) -> bool:
        obracket = {"(" : 1, "[" : 2, "{" : 3}
        cbracket = {")" : 1, "]" : 2, "}" : 3}
        stack = []
        
        for char in s:
            if char in obracket or char in cbracket:
                if char in obracket:
                    stack.append(obracket[char])
                else:
                    if stack and stack[-1] == cbracket[char]:
                        stack.pop()
                    else:
                        return False
        if not stack:
            return True
        return False
