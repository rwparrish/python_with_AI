from turtle import position


class Board:
  
  def __init__(self):
    self.cells = [" ", " ", " ", " ", " ", " "," ", " ", " "] 
  
  def reset(self):
    self.cells = [" ", " ", " ", " ", " ", " "," ", " ", " "]
    
  def display(self):
    print(f'''
          {self.cells[0]} | {self.cells[1]} | {self.cells[2]}
          ---------
          {self.cells[3]} | {self.cells[4]} | {self.cells[5]}
          ---------
          {self.cells[6]} | {self.cells[7]} | {self.cells[8]}
           ''')
    
  def position(self, input):
    user_input = int(input) - 1
    return self.cells[user_input]
  
  def update(self, num, player):
    index = self.position(num)
    self.cells[index] = player.token
    
  def full(self):
    return " " in self.cells
  
  def turn_count(self):
    return 9 - self.cells.count(" ")
  
  def taken(self, string):
    index = self.position(string)
    return self.cell[index] != " "
    
  def valid_move(self, string):
    return int(string) in range(1, 10) and not(self.taken(string))
  
  
  
    
    
    
    
    
  
  
    
  
    