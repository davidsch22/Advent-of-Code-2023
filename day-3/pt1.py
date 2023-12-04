def isSymbol(char: str):
    return not char.isdigit() and char != '.'


file = open('pt1.txt', 'r')
lines = file.readlines()
file.close()

total = 0

for i in range(len(lines)):
    line = lines[i].replace('\n', '')
    prev_line = None
    next_line = None
    if i != 0:
        prev_line = lines[i-1]
    if i != len(lines) - 1:
        next_line = lines[i+1]

    num = ''
    num_complete = False
    is_part = False
    for i, c in enumerate(line):
        if c == '.':
            if num != '':
                num_complete = True
                if prev_line != None and isSymbol(prev_line[i]):
                    is_part = True
                if next_line != None and isSymbol(next_line[i]):
                    is_part = True
            else:
                if is_part:
                    is_part = False
        elif c.isdigit():
            if prev_line != None:
                if isSymbol(prev_line[i]):
                    is_part = True
                if num == '' and i != 0:  # First digit
                    if isSymbol(prev_line[i-1]):
                        is_part = True
            if next_line != None:
                if isSymbol(next_line[i]):
                    is_part = True
                if num == '' and i != 0:  # First digit
                    if isSymbol(next_line[i-1]):
                        is_part = True
            num += c
        else:  # Symbol
            is_part = True
            if num != '':
                num_complete = True

        if num_complete:
            if is_part:
                total += int(num)
                if not isSymbol(c):
                    is_part = False
            num = ''
            num_complete = False
    if num != '':  # Last char in line was digit
        if is_part:
            total += int(num)
            is_part = False
        num = ''
        num_complete = False

print(total)
