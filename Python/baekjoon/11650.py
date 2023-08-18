"https://www.acmicpc.net/problem/11650"


import os 
import sys



if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline().rstrip())

coordinates = []
for _ in range(N):
    a, b = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    coordinates.append([a,b])
coordinates.sort(key=lambda x:(x[0], x[1]))

for coor in coordinates:
    print(coor[0], coor[1] )