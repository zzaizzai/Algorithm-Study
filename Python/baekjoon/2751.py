"https://www.acmicpc.net/problem/2751"

import sys
import os

if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline().rstrip())


arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))

for i in sorted(arr):
    print(i)