"https://www.acmicpc.net/problem/1181"


import sys
import os

if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline().rstrip())

words_set = set()

for _ in range(N):
    words_set.add(str(sys.stdin.readline().rstrip()))

words_list = list(words_set)
words_list.sort(key=lambda x:(len(x) , x))
# print(words_list)
for word in words_list:
    print(word)