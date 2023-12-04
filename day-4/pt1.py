def score(n):
    return 2 ** (n-1)


file = open('pt1.txt', 'r')
lines = file.readlines()
file.close()

total = 0

for line in lines:
    card = line.split(':')
    card_id = card[0].split()[1]

    card_nums = card[1].split('|')
    winning_nums = card_nums[0].split()
    have_nums = card_nums[1].split()
    
    n = 0
    for num in have_nums:
        if num in winning_nums:
            n += 1

    if n > 0:
        total += score(n)
print(total)