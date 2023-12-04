file = open('pt2.txt', 'r')
lines = file.readlines()
file.close()

total = 0
copies = {}

for line in lines:
    card = line.split(':')
    card_id = int(card[0].split()[1])

    card_nums = card[1].split('|')
    winning_nums = card_nums[0].split()
    have_nums = card_nums[1].split()
    
    n = 0
    for num in have_nums:
        if num in winning_nums:
            n += 1
    
    for i in range(card_id+1, card_id+n+1):
        if i in copies.keys():
            copies[i] += 1
        else:
            copies[i] = 1

        if card_id in copies.keys():
            copies[i] += copies[card_id]
    
    if card_id in copies.keys():
        total += copies[card_id]
    total += 1
print(total)