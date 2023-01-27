import numpy as np

def train(X, Y):
  w1 = np.random.random((100,10))
  w2 = np.random.random((10,100))
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
  print(np.round(b,1).reshape(10,10))

if __name__ == "__main__":
    with open("maze.npy", "rb") as maze:
        maze = np.load(maze)
        maze = maze.astype(np.int64)
        X = []
        X.append(maze)
        X = np.array(X)
    with open("maze_path.npy", "rb") as maze_path:
        maze_path = np.load(maze_path)
        maze_path = maze_path.astype(np.int64)
        Y = []
        Y.append(maze_path)
        Y = np.array(maze_path)
    test = X
    main()