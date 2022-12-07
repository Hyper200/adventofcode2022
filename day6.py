with open('day6_input.txt') as f:
    lines = f.read()

print(lines)

lines = list(lines)

print(lines)

initial_start = 0
max_lines=len(lines)
for x in range(initial_start, max_lines):

    first_char = initial_start
    second_char = initial_start + 1
    third_char = initial_start + 2
    forth_char = initial_start + 3

    print(lines[first_char] + lines[second_char] + lines[third_char] + lines[forth_char])

    initial_start = initial_start + 1
