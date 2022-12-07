with open('day6_input.txt') as f:
    lines = f.read()

print(lines)

lines = list(lines)

print(lines)

initial_start = 0
max_lines=len(lines)

marker = None

for i in range(initial_start,max_lines - 4):
    first_char = initial_start
    second_char = initial_start + 1
    third_char = initial_start + 2
    forth_char = initial_start + 3

    check = list(lines[first_char] + lines[second_char] + lines[third_char] + lines[forth_char])
    print(check)

    if (lines[first_char] not in check[1]) and (lines[first_char] not in check[2]) and (lines[first_char] not in check[3]) \
    and (lines[second_char] not in check[0]) and (lines[second_char] not in check[2]) and (lines[second_char] not in check[3]) \
    and (lines[third_char] not in check[0]) and (lines[third_char] not in check[1]) and (lines[third_char] not in check[3]) \
    and (lines[forth_char] not in check[0]) and (lines[forth_char] not in check[1]) and (lines[forth_char] not in check[2]):
        print(check)
        marker = initial_start + 4

    initial_start = initial_start + 1


    if marker is not None:
        break

print(marker)
