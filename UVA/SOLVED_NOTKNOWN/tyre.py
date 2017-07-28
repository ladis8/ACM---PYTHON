
from sys import stdin
def count (inp):
  try:
      input = inp.split()
      w = int (input[1])
      h = int (input [3])
      c = int (input [5]) if len(input)== 6 else int (input[6])

      out = 3.141592 * ((2* w * h /100) +25.4 * c)
      out /=10
      print (inp, end=": ")
      print(round(out))
      return True
  except Exception:
      return False



def init ():
    line = stdin.readline().rstrip()
    while True:
        try:
           if not count (line):
               break
           line = stdin.readline().rstrip()
        except EOFError:
            break

init()
