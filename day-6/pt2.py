file = open('pt2.txt', 'r')
lines = file.readlines()
file.close()

time_line = lines[0].split(':')
dist_line = lines[1].split(':')

merged_times = time_line[1].strip().replace(' ', '')
merged_distances = dist_line[1].strip().replace(' ', '')

time = int(merged_times)
record = int(merged_distances)

total = 0

for i in range(time):
    speed = i
    remaining_time = time - i
    distance = speed * remaining_time
    if distance > record:
        total += 1

print(total)