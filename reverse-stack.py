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

def insertAtBottom(stack, item):
    if isEmpty(stack):
        push(stack, item)
    else:
        temp = pop(stack)
        insertAtBottom(stack, item)
        push(stack, temp)

def reverse(stack):
    if not isEmpty(stack):
        temp = pop(stack)
        reverse(stack)
        insertAtBottom(stack, temp)

        
stack = createStack()
push(stack,4)
push(stack,3)
push(stack,2)
push(stack,1)
print("created stack is:")
print(stack)
insertAtBottom(stack, 5)
insertAtBottom(stack, 6)
insertAtBottom(stack, 7)
print("modified stack is :")
print(stack)
reverse(stack)
print("stack after reverse is: ")
print(stack)

