n = int(input())

cards = list(range(1, n + 1))

while True:
    if len(cards) == 1:
        print(cards[0])
        break
    if len(cards) % 2 == 0:
        cards = [card for i, card in enumerate(cards) if i % 2 == 1]
    else:
        cards.pop(0)
        cards.append(cards.pop(0))
