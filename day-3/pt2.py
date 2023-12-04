def parseLine(line: str, fromIndex: int) -> list:
    nums = []
    left_checked = False
    middle_checked = False
    right_checked = False

    if fromIndex == 0:
        left_checked = True
    elif fromIndex == len(line) - 1:
        right_checked = True

    if not left_checked and line[fromIndex - 1].isdigit():  # Left side
        num = ''
        i = fromIndex - 1
        while i >= 0 and line[i].isdigit():
            num = line[i] + num
            i -= 1
        i = fromIndex
        while i < len(line) and line[i].isdigit():
            if i == fromIndex + 1:
                right_checked = True
            num += line[i]
            i += 1
        nums.append(int(num))
        middle_checked = True

    if not middle_checked and line[fromIndex].isdigit():  # Middle
        num = ''
        i = fromIndex
        while i < len(line) and line[i].isdigit():
            num += line[i]
            i += 1
        nums.append(int(num))
        right_checked = True

    if not right_checked and line[fromIndex + 1].isdigit():  # Right side
        num = ''
        i = fromIndex + 1
        while i < len(line) and line[i].isdigit():
            num += line[i]
            i += 1
        nums.append(int(num))
    return nums


file = open('pt2.txt', 'r')
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

    for i, c in enumerate(line):
        if c == '*':
            nums = []

            if i != 0 and line[i-1].isdigit():  # Left of *
                num = ''
                j = i - 1
                while j >= 0 and line[j].isdigit():
                    num = line[j] + num
                    j -= 1
                nums.append(int(num))
            if i != len(line)-1 and line[i+1].isdigit():  # Right of *
                num = ''
                j = i + 1
                while j < len(line) and line[j].isdigit():
                    num += line[j]
                    j += 1
                nums.append(int(num))
            if prev_line != None:  # Above *
                prev_nums = parseLine(prev_line, i)
                for num in prev_nums:
                    nums.append(num)
            if next_line != None:  # Below *
                next_nums = parseLine(next_line, i)
                for num in next_nums:
                    nums.append(num)

            if len(nums) == 2:
                total += (nums[0] * nums[1])

print(total)
