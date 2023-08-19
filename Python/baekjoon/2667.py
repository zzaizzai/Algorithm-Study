"https://www.acmicpc.net/problem/2667"


import sys
import os
from collections import deque


if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline().rstrip())

graph = []

for _ in range(N):
    graph.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def solution(graph) -> list[int]:

    def infection(x, y, site) -> list[int]:
        graph[x][y] = site
        q = deque()
        q.append((x, y))

        while q:
            # print(*q)
            X, Y = q.popleft()

            for i in range(4):
                nx = X + dx[i]
                ny = Y + dy[i]

                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue

                if graph[nx][ny] == 1:
                    graph[nx][ny] = site
                    q.append((nx, ny))

    site = 2
    for x in range(N):
        for y in range(N):

            if graph[x][y] == 0:
                continue

            if graph[x][y] == 1:
                # 부분적으로 바이러스가 퍼지게
                infection(x, y, site)
                site += 1

    ans_list = [0] * site
    for number in range(2, site):
        
        for gg in graph:
            ans_list[number] +=  gg.count(number)

    print(site - 2)
    ans_list.sort()
    for i in ans_list:
        if i != 0:
            print(i)

    return graph

solution(graph)

# for gg in solution(graph):
#     print(gg)
