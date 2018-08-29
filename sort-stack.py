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

def peek(stack):
    if not isEmpty(stack):
        return stack[-1]
    
def sortStack(stack):
    if not isEmpty(stack):
        temp = pop(stack)
        sortStack(stack)
        sortedInsert(stack, temp)

def sortedInsert(stack, element):
    if(isEmpty(stack) or element >= peek(stack)):
        push(stack, element)

    elif(element < peek(stack)):
        new = pop(stack)
        sortedInsert(stack, element)
        push(stack, new)


stack = createStack()
push(stack, 16)
push(stack, 25)
push(stack, 3)
push(stack, 14)
print("created stack is :")
print(stack)
sortStack(stack)
print("sorted stack is:")
print(stack)
