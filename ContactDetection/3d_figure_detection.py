import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


# -----------------generador de figura geometricas 2d------------

def genfig():
    '''
    vectorx = random.sample(range(30), 2)
    vectory = random.sample(range(30), 2)
    vectorz = random.sample(range(30), 2)
    '''
    vectorx = np.array([1, 16])
    vectory = np.array([2, 22])
    vectorz = np.array([1, 11])

    return (vectorx, vectory, vectorz)


def genpunto():
    punto = random.sample(range(30), 3)
    # punto = np.array([5, 13])
    return punto


def genarista():
    '''
    vectorx = random.sample(range(30), 2)
    vectory = random.sample(range(30), 2)
    vectorz = random.sample(range(30), 2)
    '''    
    vectorx = np.array([5, 25])
    vectory = np.array([9, 20])
    vectorz = np.array([15, 5])

    return vectorx, vectory, vectorz


def getvertex(figura):
    vertex0 = np.array([figura[0][0],
                        figura[1][0],
                        figura[2][0]])

    vertex1 = np.array([figura[0][1],
                        figura[1][0],
                        figura[2][0]])

    vertex2 = np.array([figura[0][0],
                        figura[1][1],
                        figura[2][0]])

    vertex3 = np.array([figura[0][0],
                        figura[1][0],
                        figura[2][1]])
    return (vertex0, vertex1, vertex2, vertex3)


def getB(figura):
    vertex = np.array(getvertex(figura))
    U0 = np.array(vertex[0])
    U1 = np.array(vertex[1])
    U2 = np.array(vertex[2])
    U3 = np.array(vertex[3])
    # ----------------------------------------
    b1 = U1 - U0
    b2 = U2 - U0
    b3 = U3 - U0

    normb1 = np.linalg.norm(b1, ord=2)
    normb2 = np.linalg.norm(b2, ord=2)
    normb3 = np.linalg.norm(b3, ord=2)

    b1v = (b1 / normb1)
    b2v = (b2 / normb2)
    b3v = (b3 / normb3)

    B = np.array([[b1v[0], b1v[1], b1v[2]],
                  [b2v[0], b2v[1], b2v[2]],
                  [b3v[0], b3v[1], b3v[2]]])
    return B, normb1, normb2, normb3


def pointdetection(figura, punto):
    vertex = np.array(getvertex(figura))
    U0 = np.array(vertex[0])
    U1 = np.array(vertex[1])
    U2 = np.array(vertex[2])
    U3 = np.array(vertex[3])

    # ----------------------------------------
    a = U1 - U0
    c = U2 - U0
    b = U3 - U0

    B = getB(figura)

    V0 = punto[0] - U0[0]
    V1 = punto[1] - U0[1]
    V2 = punto[2] - U0[2]

    V = np.array([[V0], [V1], [V2]])

    alpha = np.linalg.solve(B, V)

    resultx, resulty, resultz = False, False, False

    if (0 <= alpha[0] <= max(a)):
        resultx = True
    if (0 <= alpha[1] <= max(c)):
        resulty = True
    if (0 <= alpha[2] <= max(b)):
        resultz = True
    return resultx and resulty and resultz


def getRo(Vj, Vk, s):
    return (((1 - s) * Vj) + (s * Vk))


def getS(Vj, Vk, a, b, c):
    q = np.zeros((3, 2))
    q[0][1] = a
    q[1][1] = b
    q[2][1] = c
    p = np.array(Vj)
    w = np.array(Vk - Vj)
    s = np.zeros((3, 2))
    print("q:\n", q, "\np:\n", p, "\nw\n:", w)
    for i in range(0, 3):
        s[i] = (q[i] - p[i]) / w[i]
    return s


def aristaisinside(ro1, ro2, a, b, c):
    s = [[0, 0], [0, 0], [0, 0]]
    # -----------------Vj--------------
    if (0 <= ro1[0] <= a):
        s[0][0] = ro1[0]
    else:
        s[0][0] = []
    if (0 <= ro1[1] <= b):
        s[1][0] = ro1[1]
    else:
        s[1][0] = []
    if (0 <= ro1[2] <= c):
        s[2][0] = ro1[2]
    else:
        s[2][0] = []
        # ------------Vk-------------
    if (0 <= ro2[0] <= a):
        s[0][1] = ro2[0]
    else:
        s[0][1] = []
    if (0 <= ro2[1] <= b):
        s[1][1] = ro2[1]
    else:
        s[1][1] = []
    if (0 <= ro2[2] <= c):
        s[2][1] = ro2[2]
    else:
        s[2][1] = []
    return s


def aristadetection(figura, arista):
    # ----------------------- get vectores de las figuras---------------------------------
    vertex = np.array(getvertex(figura))
    U0 = np.array(vertex[0])
    U1 = np.array(vertex[1])
    U2 = np.array(vertex[2])
    U3 = np.array(vertex[3])
    # -----------------------get vectores de las aristas---------------------------------
    Vj = np.array([arista[0][0], arista[1][0], arista[2][0]])
    Vk = np.array([arista[0][1], arista[1][1], arista[2][1]])
    Vjprima = Vj - U0
    Vkprima = Vk - U0
    B = getB(figura)

    r1 = getRo(Vjprima, Vkprima, 0)
    ro1 = np.linalg.solve(B[0], r1)

    r2 = getRo(Vjprima, Vkprima, 1)
    ro2 = np.linalg.solve(B[0], r2)

    a = B[1]  # para cambio en eje X
    b = B[2]  # para cambio en eje Y
    c = B[3]  # para cambio en eje Z

    s = getS(Vjprima, Vkprima, a, b, c)
    print("s antes de ser ordenada :\n", s)
    J = aristaisinside(ro1, ro2, a, b, c)

    Si = np.array([[s[0][0] - Vj[0]],
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
        return J, True, s, Vjprima, Vkprima


# ----------main----------------

# punto = genpunto()
figura = genfig()
arista = genarista()

xline = np.array(figura[0])
yline = np.array(figura[1])
zline = np.array(figura[2])

xarista = np.array(arista[0])
yarista = np.array(arista[1])
zarista = np.array(arista[2])

U0 = np.array(getvertex(figura)[0])
# inside = pointdetection(figura, punto)
s, aristadentro, dentro, Vjp, Vkp = aristadetection(figura, arista)

print("s:\n", s, "\n arista dentro??:\n", aristadentro, "\narista dentro:\n", dentro)
dentro = np.sort(dentro)
print("s ordenado:\n", dentro)
Si = np.max(dentro[:, 0])
Sf = np.min(dentro[:, 1])
print("si:\n", Si, "\nSf:\n", Sf)
Si = Vjp + Si * (Vkp - Vjp) + U0
Sf = Vjp + Sf * (Vkp - Vjp) + U0

'''segdentro = np.array([[dentro[0][0], dentro[1][0]],
                      [dentro[0][1], dentro[1][1]],
                      [dentro[0][2], dentro[1][2]]])
print(segdentro,s)
''''''
segmentocompleto = np.array([xarista, yarista, zarista])
fuera = segmentocompleto - s
segmentofuera = np.array(1)
print("\nsegmento completo:\n", segmentocompleto,
      "\n fuera: \n", fuera,
      "\nsegmento fuera:\n", segmentofuera)
'''
# ----------------------------Config Plano catersiano----------------------
ax = plt.axes(projection='3d')
ax.set_xlim3d(0, 30)
ax.set_ylim3d(0, 30)
ax.set_zlim3d(0, 30)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# ----------------------------Dibujo 3d--------------------------
ax.plot3D((xline[0], xline[1], xline[1], xline[0], xline[0]),
          (yline[0], yline[0], yline[1], yline[1], yline[0]),
          zline[0],
          color='m')
ax.plot3D((xline[0], xline[1], xline[1], xline[0], xline[0]),
          (yline[0], yline[0], yline[1], yline[1], yline[0]),
          zline[1],
          color='c')
ax.plot3D((xline[0], xline[0]),
          (yline[0], yline[0]),
          (zline[0], zline[1]),
          color='r')
ax.plot3D((xline[1], xline[1]),
          (yline[0], yline[0]),
          (zline[0], zline[1]),
          color='r')
ax.plot3D((xline[1], xline[1]),
          (yline[1], yline[1]),
          (zline[0], zline[1]),
          color='r')
ax.plot3D((xline[0], xline[0]),
          (yline[1], yline[1]),
          (zline[0], zline[1]),
          color='r')

# ----------------------------- Dibuja un punto decolor verde si esta dentro y si esta fuera de rojo -----------------------
'''if(inside):
    ax.plot3D((punto[0], punto[0]),
              (punto[1], punto[1]),
              (punto[2], punto[2]),
              'o',
              color = 'g')
else:
    ax.plot3D((punto[0], punto[0]),
              (punto[1], punto[1]),
              (punto[2], punto[2]),
              'o',
              color='r')
'''  # -----------------------------------Dibuja la arista-------------------
if (aristadentro):
    ax.plot3D((xarista[0], xarista[1]),
              (yarista[0], yarista[1]),
              (zarista[0], zarista[1]),
              'o-',
              color='y')
    '''ax.plot3D((segdentro[0]),
              (segdentro[1]),
              (segdentro[2]),
              'o-',
              color='c')'''
else:
    ax.plot3D((xarista[0], xarista[1]),
              (yarista[0], yarista[1]),
              (zarista[0], zarista[1]),
              'o-',
              color='b')
    ax.plot3D((Si[0], Sf[0]),
              (Si[1], Sf[1]),
              (Si[2], Sf[2]),
              'o-',
              color='c')
'''    
ax.plot3D((xarista[0], sprima[0]),
(yarista[0], sprima[1]),
(zarista[0], sprima[2]),
'o-',
color = 'y')
'''
plt.grid()
plt.show()

