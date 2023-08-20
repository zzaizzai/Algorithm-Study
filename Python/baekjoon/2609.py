"https://www.acmicpc.net/problem/2609"


import os
import sys
import math

if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")

a, b = map(int, input().split())

# gcd = -1
# lcm = -1

# for i in range(max(a, b), 0, -1):
#     if a % i == 0 and b % i == 0:
#         gcd = i
#         break

# for i in range(max(a, b), a*b + 1):
#     if i % a == 0 and i % b == 0:
#         lcm = i
#         break


# print(gcd)
# print(lcm)

print(math.gcd(a,b))
print(math.lcm(a,b))
