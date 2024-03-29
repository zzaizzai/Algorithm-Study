from collections import deque
import os
import sys

if os.path.exists("input.txt"):
    sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())

maze = []

for _ in range(N):
    maze.append(list(map(int, input())))

for gra in maze:
    print(gra)

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))

    # while queue:
    for _ in range(10):
        print(*queue)
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # if nx < 0 or nx >= N or ny < 0 or ny >= M:
            #     continue

            # if maze[nx][ny] == 0:
            #     continue

            # 벽이 아니므로 이동
            # if maze[nx][ny] == 1:
            #     maze[nx][ny] = maze[x][y] + 1
            queue.append((nx, ny))
                
    
    # 마지막 값에서 카운트 값을 뽑는다.
    return maze[N-1][M-1]


print(bfs(0, 0))

for gra in maze:
    print(gra)
