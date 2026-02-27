import random


def generate_minesweeper(rows, cols, num_mines):
    """Generate minesweeper board with mines and numbers"""

    # Initialize empty board
    board = [[0 for _ in range(cols)] for _ in range(rows)]

    # Place mines randomly
    positions = random.sample(range(rows * cols), num_mines)
    for pos in positions:
        row, col = divmod(pos, cols)
        board[row][col] = -1  # -1 represents mine

    # Calculate numbers for non-mine cells
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    for i in range(rows):
        for j in range(cols):
            if board[i][j] != -1:
                # Count adjacent mines
                mine_count = 0
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if (
                        0 <= ni < rows and
                        0 <= nj < cols and
                        board[ni][nj] == -1
                    ):
                        mine_count += 1
                board[i][j] = mine_count

    return board


def reveal_cell(board, revealed, row, col):
    """Reveal cell and propagate if it's a zero"""

    if revealed[row][col]:
        return

    revealed[row][col] = True

    # If cell is 0, reveal all adjacent cells
    if board[row][col] == 0:
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for di, dj in directions:
            ni, nj = row + di, col + dj
            if (
                0 <= ni < len(board) and
                0 <= nj < len(board[0]) and
                not revealed[ni][nj] and
                board[ni][nj] != -1
            ):
                reveal_cell(board, revealed, ni, nj)