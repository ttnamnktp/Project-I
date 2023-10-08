def is_valid(board, row, col, num):
    # Check if 'num' is already in the current row or column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check if 'num' is already in the current 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return 1  # Found a solution

    row, col = empty_cell

    count = 0
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            count += solve_sudoku(board)
            board[row][col] = 0  # Backtrack

    return count


def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def input_sudoku():
    board = []
    for i in range(9):
        row = input().split()
        board.append([int(x) for x in row])
    return board


def main():
    sudoku_board = input_sudoku()
    solutions_count = solve_sudoku(sudoku_board)
    print(f"{solutions_count}")


if __name__ == "__main__":
    main()
