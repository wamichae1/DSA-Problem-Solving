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

#Recursive
def recsortStack(stack):
    if not stack:
        return stack
    top = stack.pop()
    recsortStack(stack)
    insertInOrder(stack, top)
    return stack

def insertInOrder(stack, value):
    if not stack or stack[-1] <= value:
        stack.append(value)
        return
    top = stack.pop()
    insertInOrder(stack, value)
    stack.append(top)
