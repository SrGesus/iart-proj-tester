import random
import sys
import visualizer

def print_usage():
  script_name = sys.argv[0]
  print(f"Usage: python {script_name} <matrix_size> [options]")
  print("Options:")
  print("\t-v\t\tVisualizes the generated image")

# Possible pieces to string dictionary
LEFT, UP, DOWN, RIGHT = range(0,4)
PIECES: dict = {
#  left   up     down   right          left   up     down   right
  (False, False, False, True):  "FD", (True,  False, False, False): "FE",
  (True,  False, False, True):  "LH", (False, False, True,  False): "FB",
  (False, False, True,  True):  "VB", (True,  False, True,  False): "VE",
  (True,  False, True,  True):  "BB", (False, True,  False, False): "FC",
  (False, True,  False, True):  "VD", (True,  True,  False, False): "VC",
  (True,  True,  False, True):  "BC", (False, True,  True,  False): "LV",
  (False, True,  True,  True):  "BD", (True,  True,  True,  False): "BE",
}

class Matrix:
  def possibilities(self, i, j) -> list:
    l = PIECES.keys()
    l = [p for p in l if p[LEFT] == self.matrix[i][j-1][RIGHT]]
    l = [p for p in l if p[UP] == self.matrix[i-1][j][DOWN]]
    if i == self.n:
      l = [p for p in l if p[DOWN] == False]
    if j == self.n:
      l = [p for p in l if p[RIGHT] == False]
    return l
  
  def set_piece(self, i, j) -> bool:
    """ Changes piece i, j to random piece, assumes up and left is also set.
        Returns False if not successful; True otherwise.
    """
    p = self.possibilities(i,j)
    if len(p) == 0:
      return False
    self.matrix[i][j] = p[random.randint(0, len(p)-1)]
    return True

  def is_valid(self) -> bool:
    v, frontier = set(), [(self.n,self.n)]
    while frontier:
      f = frontier.pop()
      if (f in v):
        continue
      if self.matrix[f[0]][f[1]][LEFT] and self.matrix[f[0]][f[1]-1][RIGHT]:
        frontier.append((f[0], f[1]-1))
      if self.matrix[f[0]][f[1]][UP] and self.matrix[f[0]-1][f[1]][DOWN]:
        frontier.append((f[0]-1, f[1]))
      if self.matrix[f[0]][f[1]][DOWN] and self.matrix[f[0]+1][f[1]][UP]:
        frontier.append((f[0]+1, f[1]))
      if self.matrix[f[0]][f[1]][RIGHT] and self.matrix[f[0]][f[1]+1][LEFT]:
        frontier.append((f[0], f[1]+1))
      v.add(f)
    return self.n*self.n==len(v)

  def __init__(self, n: int):
    self.n = n
    while True:
      self.matrix = [[(False, False, False, False) for i in range(n+2)] for i in range(n+2)]
      valid = True
      for i in range(1, n+1):
        for j in range(1, n+1):
          valid &= self.set_piece(i,j)
      if valid and self.is_valid():
        self.matrix = [r[1:-1] for r in self.matrix[1:-1]]
        return

  def to_strings(self):
    for row in self.matrix:
      yield "\t".join([PIECES[p] for p in row])

  def print(self):
    for line in self.to_strings():
      print(line)

  def visualize(self):
    visualizer.visualize(self.to_strings())

def main():
  if len(sys.argv) > 1:
    try:
      arg = int(sys.argv[1])
      if (arg < 2):
        raise ValueError
      m = Matrix(arg)
      m.print()
    except ValueError:
      print_usage()
      return
  else:
    print_usage()
    return
  if len(sys.argv) > 2 and m != None:
    for o in sys.argv[1:]:
      if o == '-v':
        m.visualize()

if __name__ == "__main__":
  main()
