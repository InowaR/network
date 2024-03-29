import numpy as np
import os
import pickle

while True:
  try:
    b = np.zeros(100)
    i = 0
    while i < 40:   # number of ones
      b[i] += 1
      i += 1
    np.random.shuffle(b)
    with open('constant.txt', 'wb') as out:
      pickle.dump(b, out)
      
    maze = b.reshape(10,10)
    os.system('clear')
    print(maze)
    print("---------------------------------")
    i = 0
    while i < len(b):
      if b[i] == 0:
        b[i] += 2
      if b[i] == 1:
        if b[i+9] == 0:
          b[i+9] += 2
        if b[i+9] == 1:
          break
        i += 9
      i += 1
    indexes = np.where(b == 2)
    c = indexes[0]
    c = c[len(c)-1]
    j = c
    b[j] = 0
    if b[j+9] == 0:
      b[j+9] += 2
      j += 10
    while j < len(b):
        if b[j] == 0:
          b[j] += 2
        if b[j] == 1:
          if b[j+9] == 0:
            b[j+9] += 2 
          if b[j+9] == 1:
            break
          j += 9
        j += 1
    if b[0] == 2 and b[99] == 2:
        matrix = b.reshape(10,10)
        print(matrix)
        replaced = b
        i = 0
        while i < len(replaced):
            if replaced[i] == 1.0:
                replaced[i] = 0.0
            if replaced[i] == 2.0:
                replaced[i] = 1.0
            i += 1
        print("Save array y/n?")
        m = input()
        if m == "y":
          with open('maze_path.txt', 'ab') as out_Y:
            pickle.dump(replaced, out_Y)
          with open('constant.txt', 'rb') as constant_X:
            X = pickle.load(constant_X)
          with open('maze.txt', 'ab') as out_X:
            pickle.dump(X, out_X)

            continue
        if m == "n":
            continue
        break  

  except IndexError:
    os.system('clear')