input = []
with open("Day04INtest.txt") as f:
    for line in f:
        input.append(line.strip())

#print(input)
picks = input[0]

boards = []
board = []
for i in range(2, len(input), 6):
    for x in range(5):
        board.append([int(y) for y in input[i+x].split(' ') if y != ''])
    else:
        if board != []:
            boards.append(board)
            board = []
print(picks)
print(boards)


#set picks to -1
for pick in picks:
    for board in boards:
        for line in board:
            for i in range(len(line)):
                line[i] = -1
    #check for bingo
    for board in boards:
        #check lines
        for line in board:
            if