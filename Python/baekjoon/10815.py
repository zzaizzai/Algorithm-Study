"https://www.acmicpc.net/problem/10815"


import os 
import sys

if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline().rstrip())

a_list = [False] * (20000000 + 1)
a_list_index = list(map(int, sys.stdin.readline().rstrip().split()))
for i in a_list_index:
    a_list[i] = True

M = int(sys.stdin.readline().rstrip())

b_list = [False] * (20000000 + 1)
b_list_index = list(map(int, sys.stdin.readline().rstrip().split()))
for i in b_list_index:
    b_list[i] = True

for i in b_list_index:
    if a_list[i]:
        print(1, end=" ")
    else:
        print(0, end=" ")