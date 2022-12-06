import time

f = open("elfscalories.txt", "r")
lines = [line.rstrip() for line in f]

print(str(lines))

elfs = {}
count = 1
elf_calories = []
for line in lines:
    if line == "":
        print("Line : " + str(line) + " is empty")

        print("Elf count increased to:" + str(count))
        print(str(elf_calories))
        elfs[count] = elf_calories

        #reset the elf calories list
        elf_calories = []
        count = count + 1
    else:
        elf_calories.append(int(line))
        print("Line : " + str(line) + " is not empty")

print(str(elfs))

print("Working out the elf with the most calories")

elf_total = {}

for elf in elfs:
    print(str(elfs[elf]))
    value = sum(elfs[elf])
    print(value)
    elf_total[elf] = int(value)

print(str(elf_total))

current_value = 0
for elf in elf_total:
    if int(elf_total[elf]) > int(current_value):
        current_value = int(elf_total[elf])
        print("Elf: " + str(elf) + " is carrying : " + str(current_value) + " calories. Fat fuck")
        top_elf = elf

# remove the top_elf then find the next
bunch_of_fat_elfs = {}
bunch_of_fat_elfs[top_elf] = elf_total[top_elf]

print(str(bunch_of_fat_elfs))

del elf_total[top_elf]

print(str(elf_total))

current_value = 0
for elf in elf_total:
    if int(elf_total[elf]) > int(current_value):
        current_value = int(elf_total[elf])
        print("Elf: " + str(elf) + " is carrying : " + str(current_value) + " calories. Fat fuck")
        top_elf = elf
        print(top_elf)

bunch_of_fat_elfs[top_elf] = elf_total[top_elf]

del elf_total[top_elf]

print(str(elf_total))

current_value = 0
for elf in elf_total:
    if int(elf_total[elf]) > int(current_value):
        current_value = int(elf_total[elf])
        print("Elf: " + str(elf) + " is carrying : " + str(current_value) + " calories. Fat fuck")
        top_elf = elf
        print(top_elf)

bunch_of_fat_elfs[top_elf] = elf_total[top_elf]

print(bunch_of_fat_elfs)

print(sum(bunch_of_fat_elfs.values()))

