'''
You have an empty sequence, and you will be given  queries. Each query is one of these three types:

1   -Push the element x into the stack.
2   -Delete the element present at the top of the stack.
3   -Print the maximum element in the stack.

if we solve simply by max(stack) then for large no of elements in stack it gives
runtime error so I solved it by using node for every element of stack
'''



# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
class stackNode:
    def __init__(self, val, curMax):
        self.val = val
        self.curMax = curMax

stack = []
maxvalue = 0
for _ in range(n):
    q = list(map(int, input().split()))
    if q[0] == 1:
        maxvalue = max(maxvalue, q[1])
        stack.append(stackNode(q[1],maxvalue))
    elif q[0] == 2:
        if len(stack)>0:
            stack.pop()
        if len(stack)==0:
            maxvalue = 0
        else:
            maxvalue = stack[-1].curMax
    elif q[0]==3:
        print(stack[-1].curMax)
