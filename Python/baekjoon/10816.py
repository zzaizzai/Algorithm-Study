import os
import sys


if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline().rstrip())

a = list(map(int, sys.stdin.readline().rstrip().split()))

M = int(sys.stdin.readline().rstrip())

b = list(map(int, sys.stdin.readline().rstrip().split()))


a_have = [0] * 20000001

for i in a :
    a_have[i] += 1


for i in b:
    print(a_have[i], end=" ")