def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack)==0

def push(stack, item):
    stack.append(item)

def pop(stack):
    if(isEmpty(stack)):
        print("stack underflow")
        return
    return stack.pop()

def deleteMiddle(stack, n, curr):
        
    if(isEmpty(stack) or curr == n):
        return

    temp = pop(stack)
    deleteMiddle(stack, n, curr+1)

    if(curr != int(n/2)):
        push(stack, temp)
    
curr = 0
stack = createStack()
push(stack, 1)
push(stack, 2)
push(stack, 3)
push(stack, 4)
push(stack, 5)
print("created stack is :")
print(stack)
deleteMiddle(stack, len(stack), curr)
print("modified stack is:")
print(stack)
