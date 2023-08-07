import sys

from collections import deque


"""
問題
N x M の迷路があり、現座標は(1,1)である。
移動は１回で１座標分できるとする。
出口は(N,M)であり、与えられた迷路で0が通れない部分、1は通れる部分とする。
脱出するための最小移動回数を求めよう。
https://wooono.tistory.com/498
"""


sys.stdin = open("test_1.txt", "r")

n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int,input())))

check = [[0]*m for _ in range(n)]

count = [[0]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():

    # bfs 탐색용 큐 생성
    queue = deque()

    # 시작 위치를 큐에 삽입
    queue.append((0,0))
    # 시작 위치 방문 기록
    check[0][0] = 1
    # 시작 위치 이동칸 수 기록

    count[0][0] = 1
    while queue:
        # 큐의 최하단 요소를 현재 위치로 저장하고 큐에서 제거
        x, y = queue.popleft()

        # 현재 위치를 기준으로 상하좌우 탐색
        for i in range(4):

            # 인접한 노드의 위치
            nx = x + dx[i]
            ny = y + dy[i]

            # 인접한 노드가 미로 내부에 존재하는지 확인
            if (nx >=0 and nx < n and ny >= 0 and ny < m):

                # 인접한 노드를 방문할 수 있는지 확인
                if (check[nx][ny] == 0 and maze[nx][ny] == 1):

                    # 방문할 수 있다면 큐에 삽입
                    queue.append((nx,ny))
                    # 인접 노드 방문 기록
                    check[nx][ny] = 1
                    # 인접 노드 이동칸 수 기록
                    count[nx][ny] = count[x][y] + 1

    return count[n-1][m-1]

print(bfs())