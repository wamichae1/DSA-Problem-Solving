def sortStack(stack):
    #Sorts items of the stack, smallest on top.
    tmpStack = []
    while stack:
        num = stack.pop()
        while tmpStack and tmpStack[-1] < num:

            stack.append(tmpStack[-1])
            tmpStack.pop()
        tmpStack.append(num)
    return tmpStack
stack = [23,3,31,98,92,23]
print(sortStack(stack))