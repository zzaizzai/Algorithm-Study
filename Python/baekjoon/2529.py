"https://www.acmicpc.net/problem/2529"

import os
import sys
import itertools


if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")


def checkInequls(inequalities: list, per: tuple) -> bool:
    for i in range(len(inequalities)):
        # print(per[i], inequalities[i], per[i + 1])

        if inequalities[i] == ">":
            if not (per[i] > per[i + 1]):
                return False

        if inequalities[i] == "<":
            if not ( per[i] < per[i + 1]):
                return False

    return True


k = int(sys.stdin.readline().rstrip())

inequalities = list(map(str, sys.stdin.readline().rstrip().split(" ")))

value_max = str(0)
value_min = str(100 ** k)


arr = [i for i in range(10)]
pers = list(itertools.permutations(arr, k + 1))

for per in pers:

    if checkInequls(inequalities, per):
        value_temp = "".join(str(x) for x in per)
        if int(value_temp) > int(value_max) :
            value_max = value_temp
        if int(value_temp) < int(value_min):
            value_min = value_temp

print(value_max)
print(value_min)