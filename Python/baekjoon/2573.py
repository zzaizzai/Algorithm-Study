"https://www.acmicpc.net/problem/2573"

import sys
import os


if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")

N, M = map(int, sys.stdin.readline().rstrip().split(" "))

mountain = []
for _ in range(N):
    mountain.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))


for mou in mountain:
    print(mou)


def one_year_pass(mountain: list[list[int]]):
    temp = []
    for x_list in mountain:
        temp.append([a - 2 if a > 0 else a for a in x_list])

    return temp


print("a year")
for aa in one_year_pass(mountain):
    print(aa)


def check(mountain):
    site = 2
    temp = []
    for x_list in mountain:
        temp.append([1 if a > 0 else 0 for a in x_list])

    for t in temp:
        print(t)

    for y in range(len(mountain)):
        for x in range(len(mountain[y])):
            print(mountain[y][x])

    return


print("check")
print(check(one_year_pass(mountain)))
