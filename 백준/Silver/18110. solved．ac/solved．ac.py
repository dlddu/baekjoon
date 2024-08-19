from sys import stdin

_ = stdin.readline()

scores = sorted(list(map(int, stdin.read().split())))

cut = int(len(scores) * 0.15 + 0.5)

if cut == 0:
    cutted = scores
else:
    cutted = scores[cut:-cut]

if cutted:
    print(int(sum(cutted) / len(cutted) + 0.5))
else:
    print(0)