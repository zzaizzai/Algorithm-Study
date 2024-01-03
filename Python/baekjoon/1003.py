# https://www.acmicpc.net/problem/1003
import os
import sys

if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")

T = int(sys.stdin.readline().rstrip())

class Fibonacci():
    def __init__(self):
        self.memo = {}

    def fibonacci(self, n: int):
        if n in self.memo:
            return self.memo[n]
        if n == 0:
            self.memo[n] = (1, 0)
            return (1, 0)
        elif n == 1:
            self.memo[n] = (0, 1)
            return (0, 1)
        else:
            a, b = self.fibonacci(n - 1)
            c, d = self.fibonacci(n - 2)
            self.memo[n] = (a + c, b + d)
            return self.memo[n]

ff = Fibonacci()

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    result = ff.fibonacci(n)
    print(result[0], result[1])
    