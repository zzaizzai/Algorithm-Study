"https://www.acmicpc.net/problem/1000"


import sys
import os

if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")


a, b = map(int, input().split(" "))

print(a + b)