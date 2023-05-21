# 問題 自然数N以下のすべての素数を求めよ

from typing import List


def generate_primes(number: int) -> List[int]:

    # 素数
    primes = []

    # for文の作業を減らすために、cahceで繰り返しを減らす
    cache = {}

    for x in range(2, number + 1):
        is_prime = cache.get(x)
        if is_prime is False:
            continue

        # 素数である
        primes.append(x)
        cache[x] = True

        # x の倍数はすべて素数ではないので、cacheのFalseとして処理
        for y in range(x*2, number+1, x):
            cache[y] = False

    return primes

if __name__ == "__main__":
    print(generate_primes(100))