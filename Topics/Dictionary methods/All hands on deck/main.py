cards = {'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}

res = 0
for _ in range(6):
    x = input()
    if x in cards:
        res += int(cards[x])
    else:
        res += int(x)

print(res / 6)
