import numpy as np

def getB():
    b = np.array([[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1]])
    return b

def pointdetection(U0, a, b, c, point):
    B = getB()
    V0 = point[0] - U0[0]
    V1 = point[1] - U0[1]
    V2 = point[2] - U0[2]

    V = np.array([[V0], [V1], [V2]])

    alpha = np.linalg.solve(B, V)

    resultx, resulty, resultz = False, False, False

    if (0 <= alpha[0] <= a):
        resultx = True
    if (0 <= alpha[1] <= b):
        resulty = True
    if (0 <= alpha[2] <= c):
        resultz = True
    return resultx and resulty and resultz