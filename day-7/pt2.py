import re
from functools import cmp_to_key
from collections import Counter


def get_type(hand):
    jokers = hand.count('J')
    hand = [c for c in hand if c != 'J']
    counts = sorted(Counter(hand).values(), reverse=True)
    if not counts:
        counts = [0]
    if counts[0] + jokers == 5:
        return 6
    if counts[0] + jokers == 4:
        return 5
    if counts[0] + jokers == 3 and counts[1] == 2:
        return 4
    if counts[0] + jokers == 3:
        return 3
    if counts[0] == 2 and (jokers or counts[1] == 2):
        return 2
    if counts[0] == 2 or jokers:
        return 1
    return 0


def compare(a, b):
    type_a = get_type(a[0])
    type_b = get_type(b[0])
    if type_a > type_b:
        return 1
    if type_a < type_b:
        return -1
    for card_a, card_b in zip(a[0], b[0]):
        if card_a == card_b:
            continue
        a_wins = (cards.index(card_a) > cards.index(card_b))
        return 1 if a_wins else -1


file = open('pt2.txt', 'r')
input = file.read()
file.close()

cards = 'J23456789TQKA'
regex = r'(\w{5}) (\d+)'

hands = re.findall(regex, input)
hands.sort(key=cmp_to_key(compare))

total = 0
for rank, (_, bid) in enumerate(hands, start=1):
    total += rank * int(bid)

print(total)
