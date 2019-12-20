import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import harfang as hg

# --------- get input for the figure ---------
U0 = input()
size = input()
point = input()
Vj = input()
Vk = input()

# ----------- manage data -----------
U0 = list(map(float, U0.strip().split()))
a, b, c = list(map(float, size.strip().split()))
point = list(map(float, point.strip().split()))
Vj = list(map(float, Vj.strip().split()))
Vk = list(map(float, Vk.strip().split()))

# -------------Config Plano catersiano--------

ax = plt.axes(projection='3d')
ax.set_xlim3d(0, 30)
ax.set_ylim3d(0, 30)
ax.set_zlim3d(0, 30)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')


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
    Ro = np.array([[0, a],[0, b],[0, c]])
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


# ----------------------------------- poblar el grafico con los datos----------------------
def createfigureplot(ax):
    ax.plot3D((U0[0], U0[0] + a),
              (U0[1], U0[1]),
              (U0[2], U0[2]),
              'o-',
              color='m')
    ax.plot3D((U0[0], U0[0]),
              (U0[1], U0[1] + b),
              (U0[2], U0[2]),
              'o-',
              color='m')
    ax.plot3D((U0[0] + a, U0[0] + a),
              (U0[1], U0[1] + b),
              (U0[2], U0[2]),
              'o-',
              color='m')
    ax.plot3D((U0[0] + a, U0[0]),
              (U0[1] + b, U0[1] + b),
              (U0[2], U0[2]),
              'o-',
              color='m')
    ax.plot3D((U0[0], U0[0] + a),
              (U0[1], U0[1]),
              (U0[2] + c, U0[2] + c),
              'o-',
              color='y')
    ax.plot3D((U0[0], U0[0]),
              (U0[1], U0[1] + b),
              (U0[2] + c, U0[2] + c),
              'o-',
              color='y')
    ax.plot3D((U0[0] + a, U0[0] + a),
              (U0[1], U0[1] + b),
              (U0[2] + c, U0[2] + c),
              'o-',
              color='y')
    ax.plot3D((U0[0] + a, U0[0]),
              (U0[1] + b, U0[1] + b),
              (U0[2] + c, U0[2] + c),
              'o-',
              color='y')
    ax.plot3D((U0[0], U0[0]),
              (U0[1], U0[1]),
              (U0[2], U0[2] + c),
              'o-',
              color='c')
    ax.plot3D((U0[0] + a, U0[0] + a),
              (U0[1], U0[1]),
              (U0[2], U0[2] + c),
              'o-',
              color='c')
    ax.plot3D((U0[0] + a, U0[0] + a),
              (U0[1] + b, U0[1] + b),
              (U0[2], U0[2] + c),
              'o-',
              color='c')
    ax.plot3D((U0[0], U0[0]),
              (U0[1] + b, U0[1] + b),
              (U0[2], U0[2] + c),
              'o-',
              color='c')


# ----------------------------------- plotear arista y punto a estudiar--------------------------
def plottestpoint(ax, inside):
    if (inside):
        ax.plot3D((point[0], point[0]),
                  (point[1], point[1]),
                  (point[2], point[2]),
                  'o',
                  color='c')
    else:
        ax.plot3D((point[0], point[0]),
                  (point[1], point[1]),
                  (point[2], point[2]),
                  'o',
                  color='r')


def plottestarista(ax, Si, Sf, inside):
    if (inside):
        ax.plot3D((Vj[0], Vk[0]),
                  (Vj[1], Vk[1]),
                  (Vj[2], Vk[2]),
                  'o-',
                  color='b')
        ax.plot3D((Si[0], Sf[0]),
                  (Si[1], Sf[1]),
                  (Si[2], Sf[2]),
                  'o-',
                  color='y')
    else:
        ax.plot3D((Vj[0], Vk[0]),
                  (Vj[1], Vk[1]),
                  (Vj[2], Vk[2]),
                  'o-',
                  color='r')


# ----------------------- MAIN -------------------------------------------

print("U0: ", U0, "\nsize: ", size, "\npoint: ", point, "\nVj: ", Vj, "\nVk: ", Vk)
whichfacepoint(U0, a, b, c, point)
pointinside = pointdetection(U0, a, b, c, point)
Si, Sf, aristainside = aristadetection(U0, a, b, c, Vj, Vk)
createfigureplot(ax)
#plottestpoint(ax, pointinside)
plottestarista(ax, Si, Sf, aristainside)
plt.show()
