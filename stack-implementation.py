def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack)==0

def push(stack,item):
    stack.append(item)
    print("pushed to stack "+str(item))

def pop(stack):
    if(isEmpty(stack)):
        print("stack is empty")
    return(stack.pop())

def top(stack):
    return(stack[-1])

stack = createStack()
print(isEmpty(stack))
push(stack,1)
push(stack,2)
push(stack,3)
print(top(stack))
print(stack)
pop(stack)
print(stack)
print(isEmpty(stack))
