class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        def isnum(s):
            try:
                float(s)
                return True
            except ValueError:
                return False
        p = 0
        stack = []
        ops = {
            "+": operator.add, 
            "-": operator.sub, 
            "*": operator.mul, 
            "/": operator.truediv
            }


        while p < len(tokens):
            if isnum(tokens[p]):
                stack.append(int(tokens[p]))
            else:
                # Order matters, num1 is before num2
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(ops[tokens[p]](num1, num2))) #using in to floor/celling div towards 0
            p += 1
        return stack[0]