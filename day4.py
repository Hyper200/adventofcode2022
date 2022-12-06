with open('day4_input.txt') as f:
    lines = f.read().splitlines()

lines = list(lines)
#print(lines)

number_of_pairs = 0

for line in lines:
    line = line.split(",")
    print(line)

    range1 = line[0].split("-")
    range2 = line[1].split("-")
    
    print(range1)
    print(range2)

    range1 = list(range(int(range1[0]), int(range1[1]) + 1, 1))
    range2 = list(range(int(range2[0]), int(range2[1]) + 1, 1))

    print(range1)
    print(range2)
    
    
    # if range1 == range2:
    #     print("range 1 is exacutly the same as range 2")
    #     number_of_pairs = number_of_pairs + 1
    # else:                
    #     if all(elem in range1  for elem in range2):
    #         print("Found range 1 with range 2")
    #         number_of_pairs = number_of_pairs + 1
    #     if all(elem in range2  for elem in range1):
    #         print("Found range 2 with range 1")
    #         number_of_pairs = number_of_pairs + 1

    if any(elem in range1  for elem in range2):
        print("Found range 1 with range 2")
        number_of_pairs = number_of_pairs + 1
    elif any(elem in range2  for elem in range1):
        print("Found range 2 with range 1")
        number_of_pairs = number_of_pairs + 1

print(number_of_pairs)