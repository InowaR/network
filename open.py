import pickle
import numpy as np
with open('maze_path.txt', 'rb') as out_Y:
    Y = []
    while True:
        try:
           Y.append(pickle.load(out_Y))
        except EOFError:
            break
Y = np.array(Y)
print(Y)

with open('constant.txt', 'rb') as constant_X:
    test = []
    while True:
        try:
            test.append(pickle.load(constant_X))
        except EOFError:
            break
test = np.array(test)
print(test)

with open('maze.txt', 'rb') as out_X:
    X = []
    while True:
        try:
            X.append(pickle.load(out_X))
        except EOFError:
            break
X = np.array(X)
print(X)