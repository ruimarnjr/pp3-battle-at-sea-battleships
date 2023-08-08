import random

class GameBoard:
    def __init__(self, board):
        self.board = board


    def get_letters_and_numbers():
        letters_and_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8}
        return letters_and_numbers

    def print_board(self):
        print("  A B C D E F G H I")
        print("  +-+-+-+-+-+-+-+-+")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join.row))
            row_number += 1


