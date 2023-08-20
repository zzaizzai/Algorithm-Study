"https://www.acmicpc.net/problem/2661"


import os
import sys


if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")


n = int(sys.stdin.readline().rstrip())

case_list = []
for _ in range(n):
    case_list.append(int(input()))

print(n, case_list)