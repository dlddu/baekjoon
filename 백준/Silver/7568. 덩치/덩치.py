from sys import stdin

_ = input()
ss = list(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))


def get_rank(current):
    return len([man for man in ss if man[0] > current[0] and man[1] > current[1]]) + 1


print(*list(map(get_rank, ss)))
