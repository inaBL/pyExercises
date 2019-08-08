'''
Tic Tac Toe Ref, Checkio.

You are given a result of a game and you must determine if the game ends in a win or a draw as well as who will be the winner. Make sure to return "X" if the X-player wins and "O" if the O-player wins. If the game is a draw, return "D".
A game's result is presented as a list of strings, where "X" and "O" are players' marks and "." is the empty cell.

Input: A game result as a list of strings (unicode).
Output: "X", "O" or "D" as a string.

Precondition:
There is either one winner or a draw.
len(game_result) == 3
all(len(row) == 3 for row in game_result)
'''

from typing import List


def checkio(game_result: List[str]) -> str:
        if game_result[0][0] == game_result[0][1] == game_result[0][2] and game_result[0][0] != '.':
            return game_result[0][0]
        elif game_result[0][0] == game_result[1][0] == game_result[2][0] and game_result[0][0] != '.':
            return game_result[0][0]
        elif game_result[0][0] == game_result[1][1] == game_result[2][2] and game_result[0][0] != '.':
            return game_result[0][0]
        elif game_result[1][0] == game_result[1][1] == game_result[1][2] and game_result[1][0] != '.':
            return game_result[1][0]
        elif game_result[2][0] == game_result[2][1] == game_result[2][2] and game_result[2][0] != '.':
            return game_result[2][0]
        elif game_result[2][0] == game_result[1][1] == game_result[0][2] and game_result[2][0] != '.':
            return game_result[2][0]
        elif game_result[0][1] == game_result[1][1] == game_result[2][1] and game_result[0][1] != '.':
            return game_result[0][1]
        elif game_result[0][2] == game_result[1][2] == game_result[2][2] and game_result[0][2] != '.':
            return game_result[0][2]
        else:
            return "D"


if __name__ == '__main__':
    print("Example:")
    print(checkio(["OOX",
                   "XXO",
                   "OXX"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")