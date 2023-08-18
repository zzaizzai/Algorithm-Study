"https://www.acmicpc.net/problem/10989"

import os 
import sys



if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline().rstrip())

arr = [0] * (10000 + 1)
for i in range(N):
    arr[int(sys.stdin.readline().rstrip())] += 1

for i in range(len(arr)):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)