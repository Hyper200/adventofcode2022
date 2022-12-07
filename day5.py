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
count = 0
for i in indexes:
    count = count + 1
    print(i)
    rows[count] = []


for i in container_row:
    count = 0
    i = list(i)
    print(i)
    for index in indexes:
        count = count + 1
        print(i[index])
        if i[index] != " ":
            rows[count] += i[index]

print(rows)

commands_list = []
for i in commands:
    print(i)
    commands_list.append(i.split())
    print(commands_list)

for i in commands_list:
    print("Moving Stuff...")
    # get the list in question
    source_list_ident = int(i[3])
    number_to_move = int(i[1])
    dest_list_ident = int(i[5])

    print("Source List Ident " + str(source_list_ident))
    print("Number to Move " + str(number_to_move))
    print("Dest List Ident " + str(dest_list_ident))

    source_list = rows[source_list_ident]
    dest_list = rows[dest_list_ident]

    print("Source List " + str(source_list))
    print("Number to move " + str(number_to_move))
    print("Dest List " + str(dest_list))

    #part 1
    # # moving from list
    # for i in range(1,number_to_move + 1):
    #     print(i)
    #     moveitem = source_list[0]
    #     del source_list[0]
    #     dest_list.insert(0,moveitem)

    # part 2
    # # moving from list
    print("Source List")
    print(source_list)
    move_list = source_list[0:number_to_move]
    print("Move List")
    print(move_list)
    del source_list[0:number_to_move]
    print("New Source List")
    print(source_list)

    print("Og dest list")
    print(dest_list)
    dest_list = move_list + dest_list
    print("New dest list")
    print(dest_list)   




    print(source_list)
    print(number_to_move)
    print(dest_list)

    rows[source_list_ident] = source_list
    rows[dest_list_ident] = dest_list

    print(rows)

result = []
for i in rows:
    list = rows[i]
    print(list[0])
    result.append(str(list[0]))

result = ''.join(result)

print(result)

