import sys
import os

if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")

N = int(input())

nums_set = set()

for i in range(N):
    nums_set.add(int(input()))


for value in nums_set:
    print(value)
