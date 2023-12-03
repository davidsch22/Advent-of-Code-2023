file = open('pt1.txt', 'r')
lines = file.readlines()
file.close()

total = 0
first = None
last = None

for line in lines:
    for i, c in enumerate(line):
        if c.isdigit():
            if first == None:
                first = c
            last = c
    line_val = int(first + last)
    total += line_val
    first = None
    last = None
print(total)
