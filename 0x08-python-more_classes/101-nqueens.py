#!/usr/bin/python3
import sys

def solve_n_queens(N):
    def is_safe_to_place(pos, position_oc):
        for i in range(len(position_oc)):
            if position_oc[i] == pos or \
                    position_oc[i] - i == pos - len(position_oc) or \
                    position_oc[i] + i == pos + len(position_oc):
                return False
        return True

    def place_queens_ob(position_oc, current_row, N):
        if current_row == N:
            solutions.append(position_oc.copy())
            return
        for column in range(N):
            if is_safe_to_place(column, position_oc):
                place_queens_ob(position_oc + [column], current_row + 1, N)

    solutions = []
    place_queens_ob([], 0, N)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(N)
    for solution in solutions:
        print([[i, solution[i]] for i in range(N)])
