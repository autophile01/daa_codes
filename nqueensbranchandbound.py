def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            print(row)
        print()

def is_valid_solution(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == "Q":
            return False

    return True

def solve_n_queens(n):
    def backtrack(board, row):
        if row == n:
            solutions.append(["".join(row) for row in board])
            return

        for col in range(n):
            if is_valid_solution(board, row, col, n):
                board[row][col] = "Q"
                backtrack(board, row + 1)
                board[row][col] = "."

    solutions = []
    board = [["." for _ in range(n)] for _ in range(n)]
    backtrack(board, 0)
    return solutions

if __name__ == "__main__":
    n = int(input("Enter the size of the chessboard: "))
    solutions = solve_n_queens(n)

    if solutions:
        print("Solutions to the N-Queens puzzle:")
        print_solutions(solutions)
    else:
        print("No solutions found.")

