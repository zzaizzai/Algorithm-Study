"https://www.acmicpc.net/problem/10867"


import os 
import sys



if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline().rstrip())

numbers = list(set(map(int, sys.stdin.readline().rstrip().split(" "))))
numbers.sort()
print(' '.join(map(str, numbers)))
