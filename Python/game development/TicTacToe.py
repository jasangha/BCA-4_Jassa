board = {
    'A1': ' ', 'A2': ' ', 'A3': ' ',
    'B1': ' ', 'B2': ' ', 'B3': ' ',
    'C1': ' ', 'C2': ' ', 'C3': ' '
}
player = 1          # to initialise first player
total_moves = 0     # to count the moves
end_check = 0


def check():
    # Horizontal
    if board['A1'] == 'X' and board['A2'] == 'X' and board['A3'] == 'X':
        print('Player one won !')
        return 1
    elif board['A1'] == 'O' and board['A1'] == 'O' and board['A1'] == 'O':
        print('Player Two Won!!')
        return 1

    if board['B1'] == 'X' and board['B2'] == 'X' and board['B3'] == 'X':
        print('Player One Won!!')
        return 1
    elif board['B1'] == 'O' and board['B2'] == 'O' and board['B3'] == 'O':
        print('Player Two Won!!')
        return 1

    if board['C1'] == 'X' and board['C2'] == 'X' and board['C3'] == 'X':
        print('Player One Won!!')
        return 1
    elif board['C1'] == 'O' and board['C2'] == 'O' and board['C3'] == 'O':
        print('Player Two Won!!')
        return 1
    
    # Verticle
    if board['A1'] == 'X' and board['B1'] == 'X' and board['C1'] == 'X':
        print('Player One Won!!')
        return 1
    elif board['A1'] == 'O' and board['B1'] == 'O' and board['C1'] == 'O':
        print('Player Two Won!!')
        return 1
    
    if board['A2'] == 'X' and board['B2'] == 'X' and board['C2'] == 'X':
        print('Player One Won!!')
        return 1
    elif board['A2'] == 'O' and board['B2'] == 'O' and board['C2'] == 'O':
        print('Player Two Won!!')
        return 

    if board['A3'] == 'X' and board['B3'] == 'X' and board['C3'] == 'X':
        print('Player One Won!!')
        return 1
    elif board['A3'] == 'O' and board['B3'] == 'O' and board['C3'] == 'O':
        print('Player Two Won!!')
        return 
    
    # Daigonal
    if board['A1'] == 'X' and board['B2'] == 'X' and board['C3'] == 'X':
        print('Player One Won!!')
        return 1
    elif board['A1'] == 'O' and board['B2'] == 'O' and board['C3'] == 'O':
        print('Player Two Won!!')
        return 1
    
    if board['A3'] == 'X' and board['B2'] == 'X' and board['C1'] == 'X':
        print('Player One Won!!')
        return 1
    elif board['A3'] == 'O' and board['B2'] == 'O' and board['C1'] == 'O':
        print('Player Two Won!!')
        return 1
           
    return 0

print('A1|A2|A3')
print('- +- +-')
print('B1|B2|B3')
print('- +- +-')
print('C1|C2|C3')
print('***************************')

while True:
    print(board['A1']+'|'+board['A2']+'|'+board['A3'])
    print('-+-+-')
    print(board['B1'] + '|' + board['B2'] + '|' + board['B3'])
    print('-+-+-')
    print(board['C1'] + '|' + board['C2'] + '|' + board['C3'])
    end_check = check()
    if total_moves == 9 or end_check == 1:
        break
    while True:     # input from players
        if player == 1:  
            p1_input = input('player one')
            if p1_input.upper() in board and board[p1_input.upper()] == ' ':
                board[p1_input.upper()] = 'X'
                player = 2
                break
            # wrong input
            else:
                print('Invalid input, please try again')
                continue
        else:
            p2_input = input('player two')
            if p2_input.upper() in board and board[p2_input.upper()] == ' ':
                board[p2_input.upper()] = 'O'
                player = 1
                break
            else:  # wrong input
                print('Invalid input, please try again')
                continue
    total_moves += 1
    print('***************************')
    print()