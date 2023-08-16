"https://www.acmicpc.net/workbook/view/2418"
"https://www.acmicpc.net/problem/1978"

import sys

sys.stdin = open("1978.txt", "r")

N = int(input())
list_num = list(map(int, input().split(" ")))


def is_prime(n: int) -> bool:
    if n == 1 :
        return False

    if n == 2  or  n == 3 :
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    for number in range(2, n):
        if n % number == 0 :
            return False

    return True


count_prime = 0
for num in list_num:
    if is_prime(num):
        count_prime += 1


print(count_prime)

