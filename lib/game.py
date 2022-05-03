class Game:
  
  def __init__(self, board, player1, player2):
    self.board = board
    self.players = (player2, player1)

  def current_player(self):
    empty = self.board.count(" ")
    return self.players[empty % 2]
  
  def won(self):
    pass

  def winner(self):
    pass
