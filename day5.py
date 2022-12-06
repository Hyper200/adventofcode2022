#
# Getting the initial lists from the creates
#

with open('day5_input.txt') as f:
    lines = f.read().splitlines()

index = lines.index('')
containers=lines[:index]
commands = lines[index + 1:]

print(containers)
print(commands)

# Get the last line which should be the container markings
stacks = containers[-1:]
stacks = list(stacks[0])
print(stacks)

indexes = []
for i in stacks:
    print(i)
    if i != " ":
        indexes.append(stacks.index(i))

print(indexes)


container_row = containers[:-1]
print(container_row)

rows = {}
for i in indexes:
    print(i)
    rows[i] = []

for i in container_row:
    i = list(i)
    print(i)
    for index in indexes:
        print(i[index])
        if i[index] != " ":
            rows[index] += i[index]


commands_list = []
for i in commands:
    print(i)
    commands_list.append(i.split())
    print(commands_list)

