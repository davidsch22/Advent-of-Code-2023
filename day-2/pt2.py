file = open('pt2.txt', 'r')
lines = file.readlines()
file.close()

total = 0

for line in lines:
    colon_pos = line.find(':')
    game_id = int(line[5:colon_pos])

    max_red = 0
    max_green = 0
    max_blue = 0

    sets = line[colon_pos+1:].split(';')
    for set in sets:
        cube_colors = set.split(',')
        for cube_color in cube_colors:
            cube_color = cube_color.split()
            count = int(cube_color[0])
            color = cube_color[1]
            if color == 'red' and count > max_red:
                max_red = count
            elif color == 'green' and count > max_green:
                max_green = count
            elif color == 'blue' and count > max_blue:
                max_blue = count
    power = max_red * max_green * max_blue
    total += power
print(total)
