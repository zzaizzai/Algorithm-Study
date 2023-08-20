from collections import deque
import os
import sys

if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())

maze = []

for _ in range(N):
    maze.append(list(map(int, input())))
