import numpy as np
import random
import matplotlib.pyplot as plt


# -----------------generador de figura geometricas 2d------------

def genfig():
    '''
    vectorx = random.sample(range(30), 2)
    vectory = random.sample(range(30), 2)
    '''
    vectorx = np.array([3, 25])
    vectory = np.array([3, 25])

    return (vectorx, vectory)


def genpunto():
    punto = random.sample(range(30), 2)
    # punto = np.array([5, 13])
    return punto


def genarista():
    '''vectorx = random.sample(range(30), 2)
    vectory = random.sample(range(30), 2)'''
    vectorx = np.array([5, 15])
    vectory = np.array([5, 25])
    return vectorx, vectory


def getvertex(figura):
    vertex0 = np.array([min(figura[0]), min(figura[1])])
    vertex1 = np.array([max(figura[0]), min(figura[1])])
    vertex2 = np.array([max(figura[0]), max(figura[1])])
    vertex3 = np.array([min(figura[0]), max(figura[1])])
    return (vertex0, vertex1, vertex2, vertex3)


def getB(figura):
    vertex = np.array(getvertex(figura))
    U0 = np.array(vertex[0])
    U1 = np.array(vertex[1])
    U2 = np.array(vertex[2])
    U3 = np.array(vertex[3])
    # ----------------------------------------
    b1 = U1 - U0
    b3 = U3 - U0

    normb1 = np.linalg.norm(b1, ord=2)
    normb3 = np.linalg.norm(b3, ord=2)

    b1v = (b1 / normb1)
    b3v = (b3 / normb3)

    B = np.array([[b1v[0], b1v[1]],
                  [b3v[0], b3v[1]]])
    return B


def pointdetection(figura, punto):
    vertex = np.array(getvertex(figura))
    U0 = np.array(vertex[0])
    U1 = np.array(vertex[1])
    U2 = np.array(vertex[2])
    U3 = np.array(vertex[3])
    # ----------------------------------------
    a = U1 - U0
    b = U3 - U0

    B = getB(figura)

    V0 = punto[0] - U0[0]
    V1 = punto[1] - U0[1]

    V = np.array([[V0], [V1]])

    alpha = np.linalg.solve(B, V)

    resultx, resulty = False, False
    if (0 <= alpha[0] <= max(a)):
        resultx = True
    if (0 <= alpha[1] <= max(b)):
        resulty = True
    return resultx and resulty


def aristadetection(figura, arista):
    # ----------------------- get vectores de las figuras------------
    vertex = np.array(getvertex(figura))
    U0 = np.array(vertex[0])
    U1 = np.array(vertex[1])
    U2 = np.array(vertex[2])
    U3 = np.array(vertex[3])
    # -----------------------get vectores de las aristas--------------
    Vj = np.array([arista[0][0], arista[1][0]])
    Vk = np.array([arista[0][1], arista[1][1]])
    s = np.random.sample(1)

    rS = ((1 - s) * Vj) + s * Vk

    print(" R*(s): ", rS)

    B = getB(figura)

    ro = np.linalg.solve(B, rS)
    print(" ro: ", ro)

    a = U1 - U0
    b = U3 - U0

    resultx, resulty = False, False
    if (0 <= ro[0] <= max(a)):
        resultx = True
    if (0 <= ro[1] <= max(b)):
        resulty = True
    return resultx and resulty


pts = genpunto()
figura = np.array(genfig())
TestArista = np.array(genarista())
print("figura (eje x , eje y): ", figura)
print("arista test: ", TestArista)

vertex = np.array(getvertex(figura))
vertex0 = vertex[0]
vertex1 = vertex[1]
vertex2 = vertex[2]
vertex3 = vertex[3]

init = np.array(vertex0)
fin = np.array(vertex3)


aristainside = aristadetection(figura, TestArista)
inside = pointdetection(figura, pts)

# Generar rectangulo
# ----------Config plano cartesiano de trabajo----------------

fig, ax = plt.subplots(figsize=(10, 5))
plt.axis([0, 30, 0, 30])

# ------------------------------------- Dibuja la figura -----------------------------------
ax.plot((vertex0[0], vertex1[0], vertex2[0], vertex3[0], vertex0[0]),
        (vertex0[1], vertex1[1], vertex2[1], vertex3[1], vertex0[1]),
        'o-',
        color='g')

# ----------------------------- Dibuja un punto si esta dentro de un color y si esta fuera de otro -----------------------
if (inside):
    ax.plot(pts[0],
            pts[1],
            'o',
            color='m')
else:
    ax.plot(pts[0],
            pts[1],
            'o',
            color='r')
# ---------------------------------Dibuja arista de prueba-------------------------------
if (aristainside):
    ax.plot(TestArista[0],
            TestArista[1],
            'o-',
            color='c')
else:
    ax.plot(TestArista[0],
            TestArista[1],
            'o-',
            color='r')

plt.grid()
plt.show()
