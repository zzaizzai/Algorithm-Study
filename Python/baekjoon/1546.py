"https://www.acmicpc.net/problem/1546"


n = int(input())

scores = list(map(int, input().split(" ")))


def get_new_scores(scores: list[int])-> list[int]:
    max_val = max(scores)
    new_scores = []

    for value in scores:
        a = (value/max_val) * 100
        new_scores.append(a)


    return new_scores

ave =sum(get_new_scores(scores))/len(get_new_scores(scores))
print(ave)