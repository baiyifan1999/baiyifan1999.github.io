# stage 1
def calculate_value(board):
    """calculate the total points of the letters onthe board."""
    # make sure board is not blank.
    if not board:
        return 0
        
    # convert the letter board to individual letters.
    else:
        total_letters = sum(board, [])
        
        # calculate the sum of the points.
        sum_points = 0
        for letter in total_letters:
            if letter in "EAIONRTLSUeaionrtlsu":
                sum_points += 1
            elif letter in "DGdg":
                sum_points += 2
            elif letter in "BCMPbcmp":
                sum_points += 3
            elif letter in "FHVWYfhvwy":
                sum_points += 4
            elif letter in "Kk":
                sum_points += 5
            elif letter in "JXjx":
                sum_points += 8
            elif letter in "QZqz":
                sum_points += 10
            else:
                sum_points += 0
        
    return sum_points               

# stage 2
def words_on_board(words, board):
    """check if the words are on the board."""
    board_count = {}
    blank_count = 0

    # count the characters on board.
    for row in board:
        for char in row:
            if char == '_':
                blank_count += 1
            elif char in board_count:
                board_count[char] += 1
            else:
                board_count[char] = 1
    
    result = []

    # count the letters in words.
    for word in words:
        word_count = {}
        for char in word:
            if char in word_count:
                word_count[char] += 1
            else:
                word_count[char] = 1
    
        # calculate the needed blanks in words to fill.
        need_blank = 0
        for char in word_count:
            board_char_count = board_count.get(char, 0)
            if word_count[char] > board_char_count:
                need_blank += word_count[char] - board_char_count
    
        # compare the number of needed blanks and blanks on the board.
        if need_blank <= blank_count:
            result.append(word)
    
    return result

# stage 3
def word_on_board(word, board):
    """check if the word is on the board and return position."""
    # make sure the word is not blank.
    if not word:
        return None
        
    # translate letters on the board into a dictionary of positions.
    positions = {}
    for i in range(len(board)):
        for j in range(len(board[i])):
            positions[board[i][j]] = (i, j)           
    
    # make sure the word is on the board.
    if word[0] not in positions:
        return None
        
    result = [positions[word[0]]]

    for k in range(1, len(word)):
        current_letter = word[k]

        # calculate position of the next letter and its previous position.
        if current_letter not in positions:
            return None
        current_pos = positions[current_letter]
        previous_pos = result[-1]      

        prev_row, prev_col = previous_pos
        curr_row, curr_col = current_pos

        # make sure the current position is next to the chosen position. 
        if abs(prev_row - curr_row) + abs(prev_col - curr_col) != 1:
            return None
        result.append(current_pos)
        
    return result

# stage 4
def textoggle_move(board, word_sequence, spare_letters):
    """remove the chosen letters, make a shift 
    and fill the blanks with spare letters."""
    # make the copy of the original board.
    board_copy = []
    for row in board:
        board_copy.append(row[:])

    # substitude the letter by '#'.
    for row, col in word_sequence:
        board_copy[row][col] = '#'

    rows = len(board_copy)
    cols = len(board_copy[0])

    # shift the '#', fill the blanks with letters in spare_letters or '#'.
    for col in range(cols):
        non_hash_col = []
    
        # collect the non-hash letters.
        for row in reversed(range(rows)):
            if board_copy[row][col] != '#':
                non_hash_col.append(board_copy[row][col])
        
        # fill in the collumns.
        while len(non_hash_col) < rows:
            if spare_letters:
                non_hash_col.append(spare_letters.pop(0))
            else:
                non_hash_col.append('#')
        
        # fill in the columns backwards.
        for row in range(rows):
            board_copy[row][col] = non_hash_col[rows - 1 - row]    

    return board_copy