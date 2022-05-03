from player import Player

class Human(Player):

  def move(self, board):
    return input("Enter a move 1-9 [left to right, up to down]:")
