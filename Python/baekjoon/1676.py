

"https://www.acmicpc.net/problem/1676"

N = int(input())


def factorial(n: int) -> int:
    number = n
    result = n
    while number > 1:
        result *= number - 1
        number -= 1
    return result

def count_zero(n: int) -> int :
    n_str = str(n)
    count = 0
    for a in reversed(n_str):
        if a == "0":
            count += 1
        else:
            break 

    return count

if N == 0:
    print(0)
else:
    print(count_zero(factorial(N)))