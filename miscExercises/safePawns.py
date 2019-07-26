'''
Safe Pawns, Checkio:
A pawn may capture an opponent's piece on a square diagonally in front of it on an adjacent file, by moving to that square.
For white pawns the front squares are squares with greater row number than the square they currently occupy.

A pawn is safe if another pawn can capture a unit on that square.
We have several white pawns on the chess board and only white pawns.
You should design your code to find how many pawns are safe.

See pawns.png

Input: Placed pawns coordinates as a set of strings.

Output: The number of safe pawns as a integer.
'''


# Pawn is safe whenever it has at least 1 other pawn behind it, diagonally
def safe_pawns(pawns: set) -> int:
    safe = 0

    # converting coordinates to indexes
    p_indexes = set()
    for p in pawns:
        c = ord(p[0]) - 97
        r = int(p[1]) - 1
        p_indexes.add((c, r))

    # check if pawns in set in behind diagonal positions
    for i in p_indexes:
        if (i[0] - 1, i[1] - 1) in p_indexes:
            safe += 1
        elif (i[0] + 1, i[1] - 1) in p_indexes:
            safe += 1

    return safe


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

