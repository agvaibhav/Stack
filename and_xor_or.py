'''
ques from hacker rank
Given an array a of n distinct elements. Let m1 and m2 be the smallest and the next smallest element in the interval
where , are the bitwise operators ,  and  respectively. 
Your task is to find the maximum possible value of .
'''


#!/bin/python3

import os
import sys

#
# Complete the andXorOr function below.
#
def andXorOr(a):
    #
    # Write your code here.
    #
    stack = []
    mx = (((a[0]&a[1])^(a[0]|a[1]))&(a[0]^a[1]))
    for i in a:
        while not len(stack)==0:
            top = stack[-1] 
            op = (((i&top)^(i|top))&(i^top))
            if op>mx:
                mx = op
            if i < top:
                stack.pop()
            else:
                break
        stack.append(i)
    return mx

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = list(map(int, input().rstrip().split()))

    result = andXorOr(a)

    fptr.write(str(result) + '\n')

    fptr.close()
