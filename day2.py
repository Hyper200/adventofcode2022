A = 1 # Rock
B = 2 # Paper
C = 3 # Sissors

X = 1 # Rock
Y = 2 # Paper
Z = 3 # Sissors


player1_score = 0
player2_score = 0

# Result score
lost = 0
draw = 3
win = 6



with open('input.txt') as f:
    lines = f.read().splitlines()

for line in lines:
    rockpapersissors = line.split()
    #print(rockpapersissors)

    #Setting the player values
    player1 = rockpapersissors[0]
    player2 = rockpapersissors[1]

    #print(player1)
    #print(player2)

    #
    # Logic for working out who won
    #
    # Player 1 wins if
    # player 1: A B C
    # player 2: Z X Y
    #
    # Player 2 wins if
    # player 1: A B C
    # player 2: Y Z X
    #
    # Draw if
    # player 1: A B C
    # player 2: X Y Z


    # if (player1 == 'A' and player2 == 'Z') or (player1 == 'B' and player2 == 'X') or (player1 == 'C' and player2 == 'Y'):
    #     print('Player 1 wins:')
    #     if player1 == 'A':
    #         print("Player 1 won, with a rock")
    #         player1_score = player1_score + win + A
    #     elif player1 == 'B':
    #         print("Player 1 won, with a paper")
    #         player1_score = player1_score + win + B
    #     elif player1 == 'C':
    #         print("Player 1 won, with a paper")
    #         player1_score = player1_score + win + C
    #     else:
    #         print("Elf hit user with a glass bottle")

    #     if player2 == 'X':
    #         print("Player 2 lost, with a rock")
    #         player2_score = player2_score + lost + X
    #     elif player2 == 'Y':
    #         print("Player 2 lost, with a paper")
    #         player2_score = player2_score + lost + Y
    #     elif player2 == 'Z':
    #         print("Player 2 lost, with a paper")
    #         player2_score = player2_score + lost + Z
    #     else:
    #         print("Elf hit user with a glass bottle")            
    # elif (player1 == 'A' and player2 == 'Y') or (player1 == 'B' and player2 == 'Z') or (player1 == 'C' and player2 == 'X'):
    #     print('Player 2 Wins:')
    #     if player1 == 'A':
    #         print("Player 1 lost, with a rock")
    #         player1_score = player1_score + lost + A
    #     elif player1 == 'B':
    #         print("Player 1 lost, with a paper")
    #         player1_score = player1_score + lost + B
    #     elif player1 == 'C':
    #         print("Player 1 lost, with a paper")
    #         player1_score = player1_score + lost + C
    #     else:
    #         print("Elf hit user with a glass bottle")

    #     if player2 == 'X':
    #         print("Player 1 won, with a rock")
    #         player2_score = player2_score + win + X
    #     elif player2 == 'Y':
    #         print("Player 2 won, with a paper")
    #         player2_score = player2_score + win + Y
    #     elif player2 == 'Z':
    #         print("Player 2 won, with a paper")
    #         player2_score = player2_score + win + Z
    #     else:
    #         print("Elf hit user with a glass bottle")
    # elif (player1 == 'A' and player2 == 'X') or (player1 == 'B' and player2 == 'Y') or (player1 == 'C' and player2 == 'Z'):
    #     print("Game was a draw:")
    #     if player1 == 'A':
    #         print("Player 1 drew, with a rock")
    #         player1_score = player1_score + draw + A
    #     elif player1 == 'B':
    #         print("Player 1 drew, with a paper")
    #         player1_score = player1_score + draw + B
    #     elif player1 == 'C':
    #         print("Player 1 drew, with a paper")
    #         player1_score = player1_score + draw + C
    #     else:
    #         print("Elf hit other player with a glass bottle")  

    #     if player2 == 'X':
    #         print("Player 2 draw, with a rock")
    #         player2_score = player2_score + draw + X
    #     elif player2 == 'Y':
    #         print("Player 2 draw, with a paper")
    #         player2_score = player2_score + draw + Y
    #     elif player2 == 'Z':
    #         print("Player 2 draw, with a paper")
    #         player2_score = player2_score + draw + Z
    #     else:
    #         print("Elf hit user with a glass bottle")

    # else:
    #     print("Elfs died durning this game and the results where forgotten.")
    
    # part 2Logic for working out who won
    #
    # player 2 wins if:
    # Player 1: A B C
    # Player 2: Z Z Z

    # player 1 wins if:
    # Player 1: A B C
    # Player 2: X X X

    # Draw if:
    # Player 1: A B C
    # Player 2: Y Y Y

    if (player1 == 'A' and player2 == 'Z') or (player1 == 'B' and player2 == 'Z') or (player1 == 'C' and player2 == 'Z'):
        print('Player 2 wins:')
        if player1 == 'A':
            print("Player 2 won, with a Paper")
            player2_score = player2_score + win + B
        elif player1 == 'B':
            print("Player 2 won, with a Sissors")
            player2_score = player2_score + win + C
        elif player1 == 'C':
            print("Player 2 won, with a Rock")
            player2_score = player2_score + win + A
        else:
            print("Elf hit user with a glass bottle")        
    
    elif (player1 == 'A' and player2 == 'Y') or (player1 == 'B' and player2 == 'Y') or (player1 == 'C' and player2 == 'Y'):
        print('Player 2 draw:')
        if player1 == 'A':
            print("Player 2 draw, with a Rock")
            player2_score = player2_score + draw + A
        elif player1 == 'B':
            print("Player 2 draw, with a Sissors")
            player2_score = player2_score + draw + B
        elif player1 == 'C':
            print("Player 2 draw, with a Rock")
            player2_score = player2_score + draw + C
        else:
            print("Elf hit user with a glass bottle")     

    elif (player1 == 'A' and player2 == 'X') or (player1 == 'B' and player2 == 'X') or (player1 == 'C' and player2 == 'X'):
        print('Player 2 lost:')
        if player1 == 'A':
            print("Player 2 lost, with a Rock")
            player2_score = player2_score + lost + C
        elif player1 == 'B':
            print("Player 2 lost, with a Sissors")
            player2_score = player2_score + lost + A
        elif player1 == 'C':
            print("Player 2 lost, with a Rock")
            player2_score = player2_score + lost + B
        else:
            print("Elf hit user with a glass bottle")     
    else:
        print("Elfs died durning this game and the results where forgotten.")
    #print("Player 1 total score was " + str(player1_score))
    print("Player 2 total score was " + str(player2_score))

