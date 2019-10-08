import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


# -----------------generador de figura geometricas 2d------------

def genfig():
    '''vectorx = random.sample(range(30), 2)
    vectory = random.sample(range(30), 2)
    vectorz = random.sample(range(30), 2)
    '''
    vectorx = np.array([2,25])
    vectory = np.array([2, 25])
    vectorz = np.array([2, 25])
    return (vectorx, vectory, vectorz)

def genpunto():
    punto = random.sample(range(30), 3)
    # punto = np.array([5, 13])
    return punto

def genarista():
    vectorx = random.sample(range(30), 2)
    vectory = random.sample(range(30), 2)
    vectorz = random.sample(range(30), 2)
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
    print("\nb1:\n", b1, "\nb2:\n", b2, "\nb3:\n",b3)

    normb1 = np.linalg.norm(b1, ord=2)
    normb2 = np.linalg.norm(b2, ord=2)
    normb3 = np.linalg.norm(b3, ord=2)

    print("\nnorma1:\n", normb1, "\nnorma2:\n", normb2, "\nnorma3:\n", normb3)

    b1v = (b1 / normb1)
    b2v = (b2 / normb2)
    b3v = (b3 / normb3)

    B = np.array([[b1v[0], b1v[1], b1v[2]],
                  [b2v[0], b2v[1], b2v[2]],
                  [b3v[0], b3v[1], b3v[2]]])
    return B

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
    print("\n Alfa: \n", alpha)

    resultx, resulty, resultz = False, False, False

    if (0 <= alpha[0] <= max(a)):
        resultx = True
    if (0 <= alpha[1] <= max(c)):
        resulty = True
    if (0 <= alpha[2] <= max(b)):
        resultz = True
    return resultx and resulty and resultz

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
    a = U1 - U0 # para cambio en eje X
    b = U3 - U0 # para cambio en eje Z
    c = U2 - U0 # para cambio en eje Y

    resultx, resulty, resultz = False, False, False
    if (0 <= ro[0] <= max(a)):
        resultx = True
    if (0 <= ro[1] <= max(c)):
        resulty = True
    if (0 <= ro[2] <= max(b)):
        resultz = True
    return resultx and resulty and resultz
# ----------main----------------

punto = genpunto()
figura = genfig()
arista = genarista()

arista[0].sort()
arista[1].sort()
arista[2].sort()

figura[0].sort()
figura[1].sort()
figura[2].sort()

xline = np.array(figura[0])
yline = np.array(figura[1])
zline = np.array(figura[2])

xarista = np.array(arista[0])
yarista = np.array(arista[1])
zarista = np.array(arista[2])

inside = pointdetection(figura, punto)
aristainside = False

# ----------------------------Config Plano catersiano----------------------
ax = plt.axes(projection = '3d')
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
          color= 'm')
ax.plot3D((xline[0], xline[1], xline[1], xline[0], xline[0]),
          (yline[0], yline[0], yline[1], yline[1], yline[0]),
          zline[1],
          color = 'c')
ax.plot3D((xline[0], xline[0]),
          (yline[0], yline[0]),
          (zline[0], zline[1]),
          color = 'r')
ax.plot3D((xline[1], xline[1]),
          (yline[0], yline[0]),
          (zline[0], zline[1]),
          color = 'r')
ax.plot3D((xline[1], xline[1]),
          (yline[1], yline[1]),
          (zline[0], zline[1]),
          color = 'r')
ax.plot3D((xline[0], xline[0]),
          (yline[1], yline[1]),
          (zline[0], zline[1]),
          color = 'r')

# ----------------------------- Dibuja un punto decolor verde si esta dentro y si esta fuera de rojo -----------------------
if(inside):
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
# -----------------------------------Dibuja la arista-------------------
if(aristainside):
    ax.plot3D((xarista[0], xarista[1]),
              (yarista[0], yarista[1]),
              (zarista[0], zarista[1]),
               'o-',
              color = 'b')

else:
    ax.plot3D((xarista[0], xarista[1]),
              (yarista[0], yarista[1]),
              (zarista[0], zarista[1]),
               'o-',
              color = 'b')


'''
# ---------------------------------Dibuja arista de prueba-------------------------------
if (aristainside):
    ax.plot(TestArista[0], TestArista[1], 'o-', color='c')
else:
    ax.plot(TestArista[0], TestArista[1], 'o-', color='r')

'''

plt.grid()
plt.show()
