import numpy as np
import detectionedge as edgedetect

def whichfacepoint(U0, a, b, c, point, posvertice):
    U0 = np.array(U0)
    a = np.array([a, 0, 0])
    b = np.array([0, b, 0])
    c = np.array([0, 0, c])
    d = [a[0]/2, b[1]/2, c[2]/2, a[0]/2, b[1]/2, c[2]/2]
    centromasa = np.array(posvertice)

    vertex = np.array(point)
    pospoliedro = [a[0]/2 + U0[0], b[1]/2 + U0[1], c[2]/2 + U0[2]]
    vertexprima = vertex - pospoliedro
    centromasaprima = centromasa - pospoliedro
    disti = np.zeros(6)
    distf = np.zeros(6)
    vecnormal = [[1, 0, 0],
                 [0, 1, 0],
                 [0, 0, 1],
                 [-1, 0, 0],
                 [0, -1, 0],
                 [0, 0, -1]]

    Si, Sf, aristain = edgedetect.edge_detection(U0, a[0], b[1], c[2], centromasa, vertex)
    Siprima = Si - pospoliedro
    Sfprima = Sf - pospoliedro

    caras = ["cara x", "cara y", "cara z", "cara -x", "cara -y", "cara -z"]
    faces = [[U0, U0 + a, U0 + a + b, U0 + b],
             [U0 + b, U0 + a + b, U0 + a + b + c, U0 + b + c],
             [U0 + b + c, U0 + a + b + c, U0 + c + a, U0 + c],
             [U0 + c, U0 + c + a, U0 + a, U0],
             [U0, U0 + b, U0 + c, U0 + b + c],
             [U0 + a, U0 + a + b, U0 + a + c, U0 + a + b + c]]
    for i in range(0, 6):
        disti[i] = calculardistancia(vecnormal[i], Siprima, d[i])
        distf[i] = calculardistancia(vecnormal[i], Sfprima, d[i])

    distancia = [(disti[0], distf[0], vecnormal[0], vertex),
                 (disti[1], distf[1], vecnormal[1], vertex),
                 (disti[2], distf[2], vecnormal[2], vertex),
                 (disti[3], distf[3], vecnormal[3], vertex),
                 (disti[4], distf[4], vecnormal[4], vertex),
                 (disti[5], distf[5], vecnormal[5], vertex)]
    distancia.sort()
    caraentrante = [distancia[0][2], distancia[0][3]]
    print(caraentrante)
    return Si, Sf, True, vertex, centromasa


def calculardistancia(vecnormal, vertex, d):
    dist = np.abs(((vecnormal[0] * vertex[0]) +
                   (vecnormal[1] * vertex[1]) +
                   (vecnormal[2] * vertex[2])) - d)
    return dist


