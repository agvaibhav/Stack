'''
Ques
Alexa has two stacks of non-negative integers, stack  and stack  where index denotes the top of the stack. Alexa challenges Nick to play the following game:

In each move, Nick can remove one integer from the top of either stack  or stack .
Nick keeps a running sum of the integers he removes from the two stacks.
Nick is disqualified from the game if, at any point, his running sum becomes greater than some integer  given at the beginning of the game.
Nick's final score is the total number of integers he has removed from the two stacks.
Given , , and  for  games, find the maximum possible score Nick can achieve (i.e., the maximum number of integers he can remove without being disqualified) during each game and print it on a new line.
'''


#!/bin/python3

import os
import sys

#
# Complete the twoStacks function below.
#
def twoStacks(x, a, b):
    #
    # Write your code here.
    #
    total = 0
    atemp = []
    n = len(a)
    m = len(b)
    a = list(reversed(a))
    b = list(reversed(b))
    for i in range(n):
        val = a.pop()
        if total+val > x:
            break
        total += val
        atemp.append(val)
    maxCount = len(atemp)
    curCount = maxCount

    while m:
        if total + b[-1] <= x:
            total += b.pop()
            curCount += 1
            if curCount > maxCount:
                maxCount = curCount
            m -= 1
            continue
        if len(atemp)==0:
            break
        aval = atemp.pop()
        total -= aval
        curCount -= 1
    return(maxCount)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(x, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
