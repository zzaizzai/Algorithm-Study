"https://www.acmicpc.net/workbook/view/2418"
"https://www.acmicpc.net/problem/1929"


from typing import Generator


M, N = map(int, input().split(" "))

def generate_primes(M: int, N: int) -> Generator[int, None, None] :

    primes = [True] * (N + 1)

    for num in range(2, N + 1):
        if not primes[num]:
            continue

        if num >= M:
            yield num

        for not_prime in range(num * 2, N + 1 , num):
            primes[not_prime] = False

        

primes_list = list(generate_primes(M, N))

for prime in primes_list:
    print(prime)