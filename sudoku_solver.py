import pandas as pd

class SudokuData:
  def __init__(self, file):
    self.data = pd.read_csv(file)
  
  def _get_index(self, df):
    res = set()
    for index, row in df.iterrows():
      res.add( row['index'] )
    return res
  
  def getRow(self, num):
    row = self.data[ self.data['index'] == num ]['row'].values[0]
    tmp = self.data[ self.data['row'] == row ]
    return self._get_index(tmp)
  
  def getCol(self, num):
    col = self.data[ self.data['index'] == num ]['col'].values[0]
    tmp = self.data[ self.data['col'] == col ]
    return self._get_index(tmp)
  
  def getSquare(self, num):
    box = self.data[ self.data['index'] == num ]['box'].values[0]
    tmp = self.data[ self.data['box'] == box ]
    return self._get_index(tmp)

class Cell:
  def __init__(self, number):
    self.num     = number
    self.options = set()

    if number == 0:
      self.options = set(range(1, 10))
  
  def remove(self, numbers):
    self.options.difference_update(numbers)
  
  def removeUnique(self, numbers):
    unique = []
    for option in self.options:
      if option not in numbers:
        unique.append(option)
    
    if len(unique) == 1:
      self.num     = unique[0]
      self.options = set()
  
  def check(self):
    if len(self.options) == 1:
      self.num = self.options.pop()
  
  def __str__(self) -> str:
    if self.num == 0:
      return '_'
    else:
      return str(self.num)

class Sudoku:
  def __init__(self, matrix):
    self.matrix = []
    self.data   = SudokuData('data/sudoku_data.csv')
    if len(matrix) != 81:
      return
    
    for m in matrix:
      self.matrix.append( Cell(m) )
  
  def _getNumbers(self, index):
    row = set()
    for i in index:
      if self.matrix[i].num != 0:
        row.add( self.matrix[i].num )
    return row
  
  def getSquare(self, num):
    index = self.data.getSquare(num)
    return self._getNumbers(index)
    
  def getRow(self, num):
    index = self.data.getRow(num)
    return self._getNumbers(index)
  
  def getCol(self, num):
    index = self.data.getCol(num)
    return self._getNumbers(index)
  
  def count(self):
    qty = 0
    for m in self.matrix:
      if m.num != 0:
        qty += 1
    return qty
  
  def check(self):
    for i in range(0, len(self.matrix)):
      if self.matrix[i].num != 0:
        continue
      
      rms = self.getSquare(i).union(self.getRow(i)).union(self.getCol(i))
      self.matrix[i].remove( rms )
      self.matrix[i].check()
    return len(self.matrix) - self.count()

  def uniqueOption(self):
    for i in range(0, len(self.matrix)):
      if self.matrix[i].num != 0:
        continue

      indexs = self.data.getSquare(i)
      option = set()
      for index in indexs:
        if self.matrix[index].num != 0 or index == i:
          continue
        
        option = option.union( self.matrix[index].options )
      self.matrix[i].removeUnique( option )

      if self.matrix[i].num != 0:
        continue

      indexs = self.data.getRow(i)
      option = set()
      for index in indexs:
        if self.matrix[index].num != 0 or index == i:
          continue
        
        option = option.union( self.matrix[index].options )
      self.matrix[i].removeUnique( option )

      if self.matrix[i].num != 0:
        continue

      indexs = self.data.getCol(i)
      option = set()
      for index in indexs:
        if self.matrix[index].num != 0 or index == i:
          continue
        
        option = option.union( self.matrix[index].options )
      self.matrix[i].removeUnique( option )
    return len(self.matrix) - self.count()
  
  def __str__(self) -> str:
    qty = 0
    res = ''
    for m in self.matrix:
      res += str(m) + ' '
      qty += 1
      if qty%3 == 0:
        res += '  '
      if qty%9 == 0:
        res = res[:-3]
        res += "\n"
      if qty%27 == 0:
        res += "\n"
    res = res[:-2]
    return res