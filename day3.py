#  Day 3
with open('day3_input.txt') as f:
    lines = f.read().splitlines()

    #print(lines)

batch_size = 3
lines_batch = []

for i in range(0, len(lines), batch_size):
    inital_list = []
    for line in lines[i:i+batch_size]:
        print(line)
        inital_list.append(line)
    lines_batch.append(inital_list)

print(lines_batch)   

found_characters = []
for group in lines_batch:
    print(group)
    line1 = group[0]
    line2 = group[1]
    line3 = group[2]

    print(line1)
    print(line2)
    print(line3)

    chars = []

    for char in list(line1):
        print("Searching for char: " + str(char))
        if (char in line1 and char in line2 and char in line3):
            print("Character found: " + str(char))
            if char not in chars:
                print("Found char " + char + " in three words")
                chars.append(char)
    found_characters = found_characters + chars

# found_characters = []

# for line in lines:
#     lenght = len(line)
#     middle = lenght//2
#     first_half = line[:middle]
#     second_half = line[middle:]

#     for char in list(first_half):
#         if char in second_half:
#             found_character = char
#             break
    
#     found_characters.append(found_character) 



lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

letters = list(lower_case) + list(upper_case)

print(found_characters)
found_characters_values = []

for char in found_characters:
    value = int(letters.index(char)) + 1
    found_characters_values.append(value)

print(sum(found_characters_values))