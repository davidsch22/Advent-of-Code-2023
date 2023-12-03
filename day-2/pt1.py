file = open('pt1.txt', 'r')
lines = file.readlines()
file.close()

red_limit = 12
green_limit = 13
blue_limit = 14
total = 0

for line in lines:
    colon_pos = line.find(':')
    game_id = int(line[5:colon_pos])
    possible = True

    sets = line[colon_pos+1:].split(';')
    for set in sets:
        cube_colors = set.split(',')
        for cube_color in cube_colors:
            cube_color = cube_color.split()
            count = int(cube_color[0])
            color = cube_color[1]
            if color == 'red' and count > red_limit:
                possible = False
            elif color == 'green' and count > green_limit:
                possible = False
            elif color == 'blue' and count > blue_limit:
                possible = False
    if possible:
        total += game_id
print(total)
