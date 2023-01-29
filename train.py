import numpy as np
import pickle

def train(X, Y):
  w1 = np.random.random((100,3))
  w2 = np.random.random((3,100))
  for i in range(100):
    S1 = 1 / (1 + np.exp(-(np.dot(X, w1))))
    S2 = 1 / (1 + np.exp(-(np.dot(S1, w2))))
    S2_delta = (Y - S2) * (S2 * (1 - S2))
    S1_delta = S2_delta.dot(w2.T) * (S1 * (1 - S1))
    w1 += X.T.dot(S1_delta)
    w2 += S1.T.dot(S2_delta)
  return w1, w2

def predict(test, w1, w2):
  S1 = 1 / (1 + np.exp(-(np.dot(test, w1))))
  S2 = 1 / (1 + np.exp(-(np.dot(S1, w2))))
  return S2

def main():
  a = train(X, Y)
  w1, w2 = a
  b = predict(test, w1, w2)
  print(np.round(b,2).reshape(10,10))

if __name__ == "__main__":
  with open('maze_path.txt', 'rb') as out_Y:
      Y = []
      while True:
          try:
            Y.append(pickle.load(out_Y))
          except EOFError:
              break
  Y = np.array(Y)


  with open('constant.txt', 'rb') as constant_X:
      test = []
      while True:
          try:
              test.append(pickle.load(constant_X))
          except EOFError:
              break
  test = np.array(test)


  with open('maze.txt', 'rb') as out_X:
      X = []
      while True:
          try:
              X.append(pickle.load(out_X))
          except EOFError:
              break
  X = np.array(X)
  print(test.reshape(10,10))
  main()