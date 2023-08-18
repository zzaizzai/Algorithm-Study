"https://www.acmicpc.net/problem/10828"


import os 
import sys



if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline().rstrip())

stack = []

for _ in range(N):
    order = str(sys.stdin.readline().rstrip())

    if "push" in order:
        n = int(order.split(" ")[-1])
        stack.append(n)
        
    
    if "top" in order:
        if len(stack) > 0:
            print(stack[-1]) 
        else :
            print(-1)
        

    if "pop" in order:
        if len(stack) > 0:
            print(stack[-1])
            stack.pop(-1)
        else:
            print(-1)

    if "empty" in order:
        if len(stack) > 0:
            print(0)
        else:
            print(1)

    if "size" in order:
        print(len(stack)) 