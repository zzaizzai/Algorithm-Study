
import sys

arr = [0] * (10000 + 1)

print(sys.getsizeof(arr))
arr2 = []
for _ in range(10000):
    arr2.append(0)

print(sys.getsizeof(arr2))