import numpy as np
from fractions import Fraction
class Vector:

  def __init__(self, v_string):
    self.body = []
    self.length_col = 0
    self.length_row = 0
    try:
      if '|' not in v_string:
        columns = v_string.split(':')
        self.length_col = len(columns)
        self.length_row = len(columns[0].split(','))
        for c in columns:
          column = c.split(',')
          temp = []
          for q in column:
            temp.append(Fraction(q))
          self.body.append(temp)
      else:
        rows = v_string.split('|')
        self.length_row = len(rows)
        self.length_col = len(rows[0].split(','))
        for i in range(self.length_col):
          temp = []
          for j in range(self.length_row):
            row = rows[j].split(',')
            temp.append(Fraction(row[i]))
          self.body.append(temp)
    except Exception as e:
      print(e)
      self.error()

  def error(self):
    raise Exception('Invalid Arguments !')
    self.column = []
    self.row = []
    self.length_col = 0
    self.length_row = 0

  def to_v_string(self,ls):#Change list Vector To V String
    try:
      length_col = len(ls)
      length_row = len(ls[0])
      new_v_string = ''
      for i in range(length_col):
        for j in range(length_row):
          new_v_string += str(ls[i][j])
          if j<length_row - 1:
            new_v_string += ','
        if i< length_col - 1:
          new_v_string += ':'
      return new_v_string
    except Exception as e:
      print(e)
      return ''

  def sum(self, v2):
    result = []
    if self.length_col == v2.length_col and self.length_row == v2.length_row:
      for i in range(self.length_col):
        temp = []
        for j in range(self.length_row):
          sum = self.body[i][j] + v2.body[i][j]
          temp.append(sum)
        result.append(temp)
      new_v_string = self.to_v_string(result)
      result = [1, Vector(new_v_string)]
      return result
    else:
      result = [-1,-1]
      return result

  def multiply(self, v2):
    if self.length_col != v2.length_row:
      return [-1,-1]
    try:
      result = []
      for j in range(0,v2.length_col):
        c2 = v2.get_column(j)
        temp = []
        for i in range(0,self.length_row):
          r1 = self.get_row(i)
          sum = 0
          for a,b in zip(r1,c2):
            sum+= Fraction(a) * Fraction(b)
          temp.append(sum)
        result.append(temp)
      new_v_string = self.to_v_string(result)
      return [1, Vector(new_v_string)]
    except Exception as e:
      print(e)
      return [-1, -1]

  def get_print(self):
    
    temp = ''
    for i in range(0,self.length_row):
      temp = temp + '[\t'
      for j in range(0,self.length_col):
        if self.body[j][i] ==0:
          self.body[j][i] = abs(0)
        temp=temp + str(self.body[j][i])+'\t'
      temp = temp + ']\n'
    return temp

  def get_column(self, i):
    if i<self.length_col and i >= 0:
      return self.body[i]
    else:
      return []

  def get_row(self, i):
    if i<self.length_row and i>= 0:
      result = []
      for col in self.body:
        result.append(col[i])
      return result
    else:
      return []

  def dot(self,v2):
    if self.length_col == v2.length_col and self.length_col == 1 and self.length_row == v2.length_row:
      result = 0
      v1 = self.get_column(0)
      v2 = v2.get_column(0)
      for a,b in zip(v1,v2):
        result += a * b
      return [1,result]
    else:
      return [-1,-1]

  def length(self):
    dd = self.dot(self)
    if dd[0] == 1:
      return [1,dd[1]**(1/2)]
    else:
      return [-1,-1]

  def scalar_multiply(self,m):
    try:
      for i in range(self.length_col):
        for j in range(self.length_row):
          self.body[i][j] = self.body[i][j]* Fraction(m) 
      return [1,self]
    except:
      return [-1,-1]

  def Distance(self, v2):
    if self.length_col == v2.length_col and self.length_col == 1 and self.length_row == v2.length_row:
      v2.scalar_multiply(-1)
      a = self.sum(v2)
      if a[0] == -1:
        return [-1,-1]
      v3 = a[1]
      return v3.length()
    else:
      return [-1,-1]

  def IsSquare(self):
    return (self.length_col == self.length_row)

  def CrossTrim(self,col_a,row_b):#Help function for determinant
    if not self.IsSquare():
      return
    result = []
    for col_i in range(self.length_col):
      if col_i != col_a:
        temp_col = []
        for row_i in range(self.length_row):
          if row_i != row_b:
            temp_col.append(self.body[col_i][row_i])
        result.append(temp_col)
    r = self.to_v_string(result)
    return Vector(r)

  def express_by_row(self):
    result = []
    for i in range(0,self.length_row):
      temp = []
      for j in range(0,self.length_col):
        temp.append(self.body[j][i])
      result.append(temp)
    return result
    
  def Determinant(self):
    if not self.IsSquare():
      return 0 
    if self.length_row == 2 and self.length_col == 2:
      return self.body[0][0]*self.body[1][1] - self.body[0][1] * self.body[1][0]
    elif self.length_row == 1 and self.length_col == 1:
      return self.body[0][0]
    else:
      result = 0
      for i in range(self.length_row):
        multiplier = 1
        if (i+1) % 2 == 0:
          multiplier = -1
        trimmed = self.CrossTrim(0,i)
        result+= self.body[0][i] * multiplier * trimmed.Determinant()
      return result

  def swap(self,i,j):#Swap Row i and Row j
    for c in range(self.length_col):
      temp = self.body[c][i]
      self.body[c][i] = self.body[c][j]
      self.body[c][j] = temp

  def to_echelon(self):
    reduced = 0#rows that are reduced
    i = 0
    output = ''
    while i < self.length_col:
      non_zero_index = -1
      column = self.body[i]
      for n in range(reduced,self.length_row):#Find Non-zero row
        if column[n] != 0:
          non_zero_index = n
          break 
      if non_zero_index == -1:
        i+=1
        continue
      if non_zero_index > reduced:
        self.swap(reduced,non_zero_index)
        output+='Swap\n'+self.get_print()+'\n'
        continue
      for k in range(reduced,self.length_row):
        fraction = self.body[i][k]
        for q in range(self.length_col):
          if fraction != 0:
            self.body[q][k]/= fraction
      output+='Scaling\n'+self.get_print()+'\n'
      non_zero_row = non_zero_index
      non_zero_col = non_zero_index
      if non_zero_index != i:
        non_zero_col = i
      for a in range(self.length_row):
        if a == non_zero_row:
          continue
        NotZero = self.body[non_zero_col][a] != 0
        fraction_upper = self.body[non_zero_col][a]
        for b in range(self.length_col):
          if (a < non_zero_row) :
            to_minus = self.body[b][non_zero_row] * fraction_upper
            self.body[b][a] = self.body[b][a] - to_minus
          elif (a > non_zero_row and NotZero):
            to_minus = self.body[b][non_zero_row]
            self.body[b][a] = self.body[b][a] - to_minus
      output+='Subtraction\n'+self.get_print()+'\n'
      reduced+=1
      i+=1
    return output

  def Inverse(self):
    if self.IsSquare() and self.Determinant()!=0:
      temp_len = self.length_col
      for i in range(self.length_col):
        temp = []
        for j in range(self.length_row):
          if i==j:
            temp.append(1)
          else:
            temp.append(0)
        self.body.append(temp)
      self.length_col*=2
      output = self.to_echelon()
      self.length_col = temp_len
      self.body= self.body[temp_len:]
      return output
        
def Valid_mtx(v_string):
  if '|' not in v_string:
    columns = v_string.split(':')
    n = len(columns)
    m = len(columns[0].split(','))
    if m>10 or n>10:
      raise Exception("Matrix Too Large")
    for c in columns:
      column = c.split(',')
      if len(column) != m:
        raise Exception("Invalid Arguments")
  else:
    rows = v_string.split('|')
    m = len(rows)
    n = len(rows[0].split(','))
    if m>10 or n>10:
      raise Exception("Matrix Too Large")
    for row in rows:
      row = row.split(',')
      if len(row) != n:
        raise Exception("Invalid Arguments")
  return Vector(v_string)

if __name__ =='__main__':
  a = Vector('1,4,5')
  b = Vector('4,5,6')
  print(a.scalar_multiply(3).get_print())