"https://www.acmicpc.net/problem/1037"


import os
import sys


if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")


def check(num: int, divisors: list[int]) -> bool:

    if num in divisors:
        return False

    for i in range(2, max(divisors)):
        if (num %  i != 0) and (i in divisors):
            return False
        if (num % i == 0) and (i not in divisors):
            return False

    return True


N = int(sys.stdin.readline().rstrip())

divisors = list(map(int, sys.stdin.readline().rstrip().split()))
max_value = max(divisors)

for i in range(max_value, 1000001, max_value):
    if check(i, divisors):
        print(i)
        break
