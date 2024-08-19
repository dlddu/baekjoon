_ = input()
cards = {}
for c in input().split():
    if c not in cards:
        cards[c] = 0
    cards[c] += 1
_ = input()

nums = map(lambda x: cards[x] if x in cards else "0", input().split())

print(*nums)
