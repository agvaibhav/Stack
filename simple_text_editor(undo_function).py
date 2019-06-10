'''
In this challenge, you must implement a simple text editor. Initially, your editor contains an empty string, . You must perform  operations of the following  types:

append - Append string  to the end of .
delete - Delete the last  characters of .
print - Print the  character of .
undo - Undo the last (not previously undone) operation of type 1 or 2, reverting  to the state it was in prior to that operation.
'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
Q = int(input())
s=''
last = []
for _ in range(Q):
    q = list(input().split())
    if q[0]=='1':
        s = s+q[1]
        last.append(q)
    elif q[0]=='2':
        lastele = s[-int(q[1]):]
        s = s[:len(s)-int(q[1])]
        last.append([q[0],lastele])
    elif q[0]=='3':
        print(s[int(q[1])-1])
    elif q[0]=='4':
        l = last.pop()
        if l[0]=='1':
            s = s[:len(s)-len(l[1])]
        elif l[0]=='2':
            s = s+l[1]
