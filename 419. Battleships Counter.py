def countBattleships(board):
    """Count battleships by finding top-left corners"""
    
    if not board or not board[0]:
        return 0

    count = 0
    rows, cols = len(board), len(board[0])

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'X':
                # Check if this is the start of a new battleship
                # (no 'X' above or to the left)
                if (i == 0 or board[i - 1][j] != 'X') and \
                   (j == 0 or board[i][j - 1] != 'X'):
                    count += 1

    return count