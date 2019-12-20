import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import random
# --------------------------- end config plano -----------------------------------

# ----------------------------------get B -----------------------------------
def getB():
    b = np.array([[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1]])
    return b


# --------------------------------------- END  get b ------------------------


# ----------------------------- detection if inside ------------------------------
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


def aristadetection(U0, a, b, c, Vj, Vk):
    S = np.zeros([3, 2])
    U0 = np.asarray(U0)
    Vj = np.asarray(Vj)
    Vk = np.asarray(Vk)
    Vjprima = Vj - U0
    Vkprima = Vk - U0
    B = getB()
    Ro = np.array([[0, a],
                   [0, b],
                   [0, c]])
    W = Vkprima - Vjprima
    for i in range(0, 3):
        S[i] = (Ro[i] - Vjprima[i]) / W[i]
    S = np.sort(S)
    inside = insidedetection(S)
    if (inside):
        for i in range(0, 3):
            if (S[i][0] <= 0):
                S[i][0] = 0
            if (S[i][1] >= 1):
                S[i][1] = 1
        Si = np.max(S[:, 0])
        Sf = np.min(S[:, 1])

        Si = (Vjprima + Si * (Vkprima - Vjprima)) + U0
        Sf = (Vjprima + Sf * (Vkprima - Vjprima)) + U0
        return Si, Sf, True
    else:
        return Vj, Vk, False

    '''Si = np.array([[s[0][0] - Vj[0]],
                   [s[1][0] - Vj[1]],
                   [s[2][0] - Vj[2]]])
    print("s:\n", Si, "\n y J:\n ", J)

    if not J[0][0] or not J[1][0] or not J[2][0]:
        if not J[0][1] or not J[1][1] or not J[2][1]:
            return J, False, s, Vjprima, Vkprima
        else:
            if not J[0][0]:
                J[0][0] = a
            if not J[1][0]:
                J[1][0] = b
            if not J[2][0]:
                J[2][0] = c
            return J, True, s, Vjprima, Vkprima
    if not J[0][1] or not J[1][1] or not J[2][1]:
        if not J[0][0] or not J[1][0] or not J[2][0]:
            return J, False, s, Vjprima, Vkprima
        else:
            if not J[0][1]:
                J[0][1] = a
            if not J[1][1]:
                J[1][1] = b
            if not J[2][1]:
                J[2][1] = c
            return J, True, s, Vjprima, Vkprima
    else:
        return J, True, s, Vjprima, Vkprima'''


def insidedetection(S):
    for i in range(0, 3):
        if (S[i][0] <= 0 and S[i][1] <= 0):
            inside = False
        else:
            inside = True
    return inside


def whichfacepoint(U0, a, b, c, point):
    U0 = np.array(U0)
    a = np.array([a, 0, 0])
    b = np.array([0, b, 0])
    c = np.array([0, 0, c])
    faces = [[U0, U0 + a, U0 + a + b, U0 + b],
             [U0 + b, U0 + a + b, U0 + a + b + c, U0 + b + c],
             [U0 + b + c, U0 + a + b + c, U0 + c + a, U0 + c],
             [U0 + c, U0 + c + a, U0 + a, U0],
             [U0, U0 + b, U0 + c, U0 + b + c],
             [U0 + a, U0 + a + b, U0 + a + c, U0 + a + b + c]]
    vectornormales = genvectornormal(faces, point)
    valorabsoluto = np.zeros([6, 1])
    raiz = np.zeros([6, 1])
    distancias = np.zeros([6, 2])
    for i in range(0, 6):
        valorabsoluto[i] = (abs((vectornormales[i][0] + point[0]) + (vectornormales[i][1] + point[1]) + (vectornormales[i][2] + point[2]) + (a[0])))
        raiz[i] = (np.sqrt((vectornormales[i][0] ** 2) + (vectornormales[i][1] ** 2) + (vectornormales[i][2] ** 2)))
        distancias[i] = ((valorabsoluto[i] / raiz[i]), i)
    print(distancias)
    np.sort(distancias)


def genvectornormal(faces, point):
    prodmix = np.zeros([6, 2])
    prodmix = ([1, 0, 0],
               [0, 1, 0],
               [-1, 0, 0],
               [0, -1, 0],
               [0, 0, 1],
               [0, 0, -1])
    return prodmix



def testdetection():
    U0 = [2, 4, 2]
    a, b, c = 10, 15, 25
    countpointin, countpointout, countaristain, countaristaout = 0, 0, 0, 0
    start_time_point = time.time()
    for i in range(0, 10):
        point = list(random.sample(range(30), 3))
        pointinside = pointdetection(U0, a, b, c, point)
        if pointinside:
            countpointin = countpointin + 1
        else:
            countpointout = countpointout + 1
        i = i + 1
    elapsed_time_point = (time.time() - start_time_point)
    start_time_arista = time.time()
    for j in range(0, 10):
        Vj = list(random.sample(range(30), 3))
        Vk = list(random.sample(range(30), 3))
        Si, Sf, aristainside = aristadetection(U0, a, b, c, Vj, Vk)
        if aristainside:
            countaristain = countaristain + 1
        else:
            countaristaout = countaristaout + 1
        j = j + 1

    elapsed_time_arista = (time.time() - start_time_arista)
    print(elapsed_time_point, elapsed_time_arista, countaristain, countaristaout, countpointin, countpointout)
    return Si, Sf, pointinside, aristainside, Vj, Vk, point


