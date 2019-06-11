'''
ques
There are a number of plants in a garden. Each of these plants has been treated with some amount of pesticide. After each day, if any plant has more pesticide than the plant on its left, being weaker than the left one, it dies.

You are given the initial values of the pesticide in each of the plants. Print the number of days after which no plant dies, i.e. the time after which there are no plants with more pesticide content than the plant to their left.
'''


'''
method 1  gives right answer but times out for larger cases
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the poisonousPlants function below.
def poisonousPlants(p):
    day = 0
    while(sorted(p, reverse = True) != p):
        index = []
        for i in range(len(p)-1):
            if p[i]<p[i+1]:
                index.append(i+1)
        for j in index:
            p[j]=-1
        for k in range(len(p)):
            if -1 in p:
                p.remove(-1)
            else:
                break
        day += 1
    return day

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()




'''
method 2  doesn't give timeout except for 1 case in hacker rank
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the poisonousPlants function below.
def poisonousPlants(p):
    day = 0
    stack = [[p[0]]]
    for i in range(1,len(p)):
        if p[i]<=p[i-1]:
            stack[-1].append(p[i])
        else:
            stack.append([p[i]])
    if len(stack)==1:
        return(0)
    for j in range(1, len(stack)):
        stack[j].remove(stack[j][0])
    day += 1

    for k in range(len(stack)):
        if [] in stack:
            stack.remove([])
        else:
            break
    while(len(stack)!=1):
        i=0
        while(i<(len(stack)-1)):
            if stack[i][-1]>=stack[i+1][0]:
                stack[i]=stack[i]+stack[i+1]
                stack.remove(stack[i+1])
            else:
                i+=1
        
        if len(stack)>1:
            for j in range(1,len(stack)):
                stack[j].remove(stack[j][0])
            day += 1
            
            for k in range(len(stack)):
                if [] in stack:
                    stack.remove([])
                else:
                    break
        
    return day

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()

