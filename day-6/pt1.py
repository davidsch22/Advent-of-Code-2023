file = open('pt1.txt', 'r')
lines = file.readlines()
file.close()

time_line = lines[0].split(':')
dist_line = lines[1].split(':')

times = time_line[1].split()
distances = dist_line[1].split()

total = 1

for i in range(len(times)):
    time = int(times[i])
    record = int(distances[i])

    ways = 0

    for j in range(time):
        speed = j
        remaining_time = time - j
        distance = speed * remaining_time
        if distance > record:
            ways += 1
    
    print(ways)
    total *= ways

print(total)