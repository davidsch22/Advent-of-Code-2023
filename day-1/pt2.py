file = open('pt2.txt', 'r')
lines = file.readlines()
file.close()

num_strings = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

total = 0
first_pos = None
last_pos = None
first_char = None
last_char = None

for line in lines:
    for i, c in enumerate(line):
        if c.isdigit():
            if first_pos == None:
                first_pos = i
                first_char = c
            last_pos = i
            last_char = c
    for num_str in num_strings.keys():
        first_word_pos = line.find(num_str)
        last_word_pos = line.rfind(num_str)
        if first_word_pos != -1 and (first_pos == None or first_word_pos < first_pos):
            first_pos = first_word_pos
            first_char = num_strings[num_str]
        if last_word_pos != -1 and (last_pos == None or last_word_pos > last_pos):
            last_pos = last_word_pos
            last_char = num_strings[num_str]

    line_val = int(first_char + last_char)
    total += line_val
    first_pos = None
    last_pos = None
print(total)
