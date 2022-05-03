from player import Player
import random

class Computer(Player):
  
  def move(self, board):
    return random.randint(1,9)