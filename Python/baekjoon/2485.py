# "https://www.acmicpc.net/problem/2485"

# import os
# import sys

# if os.path.exists("input.txt"):
#     sys.stdin = open("input.txt", "r")


# def insert(num: int, coordinates: list[int]) -> list[int]:
#     len_list = []
#     for i in range(len(coordinates) - 1):
#         len_list.append(coordinates[i + 1] - coordinates[i])
#     len_value = min(len_list)
#     coordinates.sort()

#     if num not in coordinates:
#         coordinates.append(num)

#     coordinates.sort()
#     return coordinates


# N = int(sys.stdin.readline().rstrip())

# coordinates = []
# len_list = []
# results = []

# for _ in range(N):
#     coordinates.append(int(sys.stdin.readline().rstrip()))

# for i in range(len(coordinates) - 1):
#     len_list.append(coordinates[i + 1] - coordinates[i])

# len_value = min(len_list)

# ans = 0
# for i in range(min(coordinates)+ 1, max(coordinates) ):

#     coordinates = insert(i, coordinates)

# print(coordinates)
