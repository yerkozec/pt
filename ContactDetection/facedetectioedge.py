import numpy as np
import diccionariocaras as facesdic
from numpy.linalg import norm

def whichfaceedge(U0, a, b, c, Si, Sf):
    U0 = np.array(U0)
    a = np.array([a, 0, 0])
    b = np.array([0, b, 0])
    c = np.array([0, 0, c])
    d = [a[0]/2, b[1]/2, c[2]/2, a[0]/2, b[1]/2, c[2]/2]
    pospoliedro = [a[0]/2 + U0[0], b[1]/2 + U0[1], c[2]/2 + U0[2]]
    Siprima = Si - pospoliedro
    Sfprima = Sf - pospoliedro
    disti = np.zeros(6)
    distf = np.zeros(6)
    vecnormal = [[1, 0, 0],
                 [0, 1, 0],
                 [0, 0, 1],
                 [-1, 0, 0],
                 [0, -1, 0],
                 [0, 0, -1]]
    caras = ['[1,0,0]', '[0,1,0]', '[0,0,1]', '[-1,0,0]', '[0,-1,0]', '[0,0,-1]']
    for i in range(0, 6):
        disti[i] = calculardistancia(vecnormal[i], Siprima, d[i])
        distf[i] = calculardistancia(vecnormal[i], Sfprima, d[i])
    '''distancia = [(disti[0], distf[0], vecnormal[0], [Si, Sf]),
                 (disti[1], distf[1], vecnormal[1], [Si, Sf]),
                 (disti[2], distf[2], vecnormal[2], [Si, Sf]),
                 (disti[3], distf[3], vecnormal[3], [Si, Sf]),
                 (disti[4], distf[4], vecnormal[4], [Si, Sf]),
                 (disti[5], distf[5], vecnormal[5], [Si, Sf])]'''
    distancia = [(disti[0], distf[0], vecnormal[0], caras[0]),
                 (disti[1], distf[1], vecnormal[1], caras[1]),
                 (disti[2], distf[2], vecnormal[2], caras[2]),
                 (disti[3], distf[3], vecnormal[3], caras[3]),
                 (disti[4], distf[4], vecnormal[4], caras[4]),
                 (disti[5], distf[5], vecnormal[5], caras[5])]
    distancia.sort()

    for i in range(0, 6):
        if distancia[i][0] == 0:
            vectornormal = distancia[i][3]
            facei = facesdic.vectoresnormales.get(vectornormal)
            caraentrantei = (distancia[i][2])
            print("Si entra por la cara:", caraentrantei)
        elif distancia[i][1] == 0:
            vectornormal = distancia[i][3]
            facef = facesdic.vectoresnormales.get(vectornormal)
            caraentrantef = (distancia[i][2])
            print("Sf entra por la cara:", caraentrantef)
    edgeoffaces = "(%s, %s)" % (facei, facef)
    print("Las caras por la que cruza la arista:", edgeoffaces)
    whichedge = facesdic.aristas.get(edgeoffaces)
    print("la arista que componen las caras", whichedge)
    dicedges, dicfaces = dicpoliedron(U0, a, b, c)
    ei = getvertex(whichedge, dicedges)
    ua = ei[0] - pospoliedro
    ub = ei[1] - pospoliedro
    vectorresultante = calcular_vector_normal(facei, facef, dicfaces)
    posnearestpoint = productocruzentrearistas(Siprima, Sfprima, ua, ub, vectorresultante)
    posnearestpoint = posnearestpoint + pospoliedro
    print("punto mas cercano:", posnearestpoint)
    return posnearestpoint

def calculardistancia(vecnormal, vertex, d):
    dist = np.abs(((vecnormal[0] * vertex[0]) +
                   (vecnormal[1] * vertex[1]) +
                   (vecnormal[2] * vertex[2])) - d)
    return dist


def getvertex(ei, edges):
    whichvertex = "(%s)" % (ei)
    poliedronedge = edges.get(whichvertex)
    return np.array(poliedronedge)


def dicpoliedron(U0, a, b, c):
    U = {'U0': U0,
         'U1': U0 + a,
         'U2': U0 + a + c,
         'U3': U0 + c,
         'U4': U0 + b,
         'U5': U0 + b + a,
         'U6': U0 + b + a + c,
         'U7': U0 + b + c}
    edges = {
        '(e0)': [U0, U0 + a],
        '(e1)': [U0 + a, U0 + a + c],
        '(e2)': [U0 + a + c, U0 + c],
        '(e3)': [U0 + c, U0],
        '(e4)': [U0, U0 + b],
        '(e5)': [U0 + a, U0 + b + a],
        '(e6)': [U0 + a + c, U0 + a + b + c],
        '(e7)': [U0 + a + c, U0 + b + c],
        '(e8)': [U0 + b + c, U0 + b],
        '(e9)': [U0 + b, U0 + b + a],
        '(e10)': [U0 + b + a, U0 + b + a + c],
        '(e11)': [U0 + a + b + c, U0 + b + c]
    }

    faces = {'f0': ([0, -1, 0], -b / 2),
             'f1': ([1, 0, 0], -a / 2),
             'f2': ([0, 0, 1], -c / 2),
             'f3': ([-1, 0, 0], -a / 2),
             'f4': ([0, 0, -1], -c / 2),
             'f5': ([0, 1, 0], -b / 2),
             }

    return edges, faces


def calcular_vector_normal(vectorcara1, vectorcara2, dicfaces):
    vectorcara1 = dicfaces.get(vectorcara1)
    vectorcara2 = dicfaces.get(vectorcara2)
    vectorcara1 = np.array(vectorcara1)
    vectorcara2 = np.array(vectorcara2)
    vectornormalresultante = vectorcara1[0] + vectorcara2[0]
    '''print("vector normal resultante: ", vectornormalresultante)'''
    vectornormalresultante = vectornormalresultante / norm(vectornormalresultante)
    '''print("vector normal resultante: ", vectornormalresultante)'''
    return vectornormalresultante

def productocruzentrearistas(Si, Sf, ua, ub, vectorresultante):
    '''print("U's:", ub, ua, "\nS's:", Si, Sf)'''
    vi = ub - ua
    vj = Sf - Si
    '''print("V's:", vi, vj)'''
    n = np.cross(vj, vi)
    '''print("n:", n)'''
    n = n / norm(n)
    '''print("n normalizado:", n)'''
    productopunto = np.dot(n, vectorresultante)
    '''print("producto punto entre n y vectornormalresultante:", productopunto)'''
    if productopunto < 0:
        n = n * -1
        nuno = np.cross(vi, n)
        '''print(nuno)'''
        nuno = nuno / norm(nuno)
        '''print("n1:", nuno)'''
        return nearestpoint(ua, Si, nuno, vj)
    else:
        nuno = np.cross(vi, n)
        nuno = nuno / norm(nuno)
        '''print("n1:", nuno)'''
        return nearestpoint(ua, Si, nuno, vj)


def nearestpoint(ua, Si, nuno, vj):
    nearestpoint = (Si + (((np.dot(ua - Si, nuno)) / np.dot(vj, nuno)) * vj))
    '''print(nearestpoint)'''
    return nearestpoint


