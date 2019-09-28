import numpy as np
import random
import matplotlib.pyplot as plt

#-----------------generador de figura geometricas 2d------------

def genfig():
    
    vectorx = random.sample(range(30), 2)
    vectory = random.sample(range(30), 2)
    '''
    vectorx = np.array([5, 20])
    vectory = np.array([7, 13])
'''
    return (vectorx, vectory)

def genpunto():
    punto = random.sample(range(20), 2)
    #punto = np.array([5, 13])
    return punto

def pointdetection(figura,punto):
    vertex = np.array(getvertex(figura))
    U0 = np.array(vertex[0])
    U1 = np.array(vertex[1])
    U2 = np.array(vertex[2])
    U3 = np.array(vertex[3])
    #----------------------------------------
    b1 = U1 - U0
    b3 = U3 - U0
    print("\n b1: \n", b1, "\n b3:\n", b3)

    normb1 = np.linalg.norm(b1, ord=2)
    normb3 = np.linalg.norm(b3, ord=2)

    print("\n norma1: \n", normb1, "\n norma0: \n", normb3)

    b1v = (b1/ normb1)
    b3v = (b3/ normb3)

    B = np.array([[b1v[0], b1v[1]],
                [b3v[0], b3v[1]]])

    print("\n B: \n", B)
    V0 = punto[0]-U0[0]
    V1 = punto[1]-U0[1]

    V = np.array([[V0], [V1]])
    print("\n V: \n", V)
    alpha = np.linalg.solve(B, V)
    print("\n Alfa: \n", alpha)
    resultx,resulty = False, False
    if(0 <= alpha[0] <= max(b1)):
        resultx = True
    if(0 <= alpha[1] <= max(b3)):
        resulty = True
    return resultx and resulty


pts = genpunto()
figura = np.array(genfig())
print("figura (eje x , eje y): ", figura)

def getvertex(figura):
    vertex0 = np.array([min(figura[0]), min(figura[1])])
    vertex1 = np.array([max(figura[0]), min(figura[1])])
    vertex2 = np.array([max(figura[0]), max(figura[1])])
    vertex3 = np.array([min(figura[0]), max(figura[1])])
    return (vertex0,vertex1,vertex2,vertex3)

vertex = np.array(getvertex(figura))
vertex0 = vertex[0]
vertex1 = vertex[1]
vertex2 = vertex[2]
vertex3 = vertex[3]

init = np.array(vertex0)
fin = np.array(vertex3)

print("punto: ", pts)
print("vertice0: ", vertex0)
print("vertice1: ", vertex1)
print("vertice2: ", vertex2)
print("vertice3: ", vertex3)
inside = pointdetection(figura, pts)

#Generar rectangulo
fig, ax = plt.subplots(figsize=(10, 5))
plt.axis([0,30,0,30])
ax.plot((vertex0[0], vertex1[0], vertex2[0], vertex3[0]),(vertex0[1], vertex1[1], vertex2[1], vertex3[1]), 'o-', color='g')
ax.plot((init[0], fin[0]), (init[1], fin[1]), 'o-', color='b')
if(inside):
    ax.plot(pts[0], pts[1], 'o', color='m')
else:
    ax.plot(pts[0], pts[1], 'o', color='r')
plt.fill_between((vertex2[0], vertex3[0]), (vertex2[1]), vertex1[1])
plt.grid()
plt.show()
