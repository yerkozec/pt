import numpy as np


def whichfacepoint(U0, a, b, c, point):
    U0 = np.array(U0)
    a = np.array([a, 0, 0])
    b = np.array([0, b, 0])
    c = np.array([0, 0, c])
    face1 = [U0, U0 + a, U0 + a + b, U0 + b]
    arista1 = [U0, U0 + a]
    arista2 = [U0, U0 + a + b]
    faces = [[U0, U0 + a, U0 + a + b, U0 + b],
             [U0 + b, U0 + a + b, U0 + a + b + c, U0 + b + c],
             [U0 + b + c, U0 + a + b + c, U0 + c + a, U0 + c],
             [U0 + c, U0 + c + a, U0 + a, U0],
             [U0, U0 + b, U0 + c, U0 + b + c],
             [U0 + a, U0 + a + b, U0 + a + c, U0 + a + b + c]]
    vectornormales = np.cross(arista1, arista2)
    print(vectornormales)
    valorabsoluto = np.zeros([6, 1])
    raiz = np.zeros([6, 1])
    distancias = np.zeros([6, 2])
    for i in range(0, 6):
        print(abs((vectornormales[i][0] + point[0]) + (vectornormales[i][1] + point[1]) + (vectornormales[i][2] + point[2]) + (a[0])))
        print(np.sqrt((vectornormales[i][0] ** 2) + (vectornormales[i][1] ** 2) + (vectornormales[i][2] ** 2)))




if __name__ == '__main__':
    U0 = [4, 5, 6]
    size = [10, 15, 20]
    point = [10, 10, 11]
    whichfacepoint(U0, size[0], size[1], size[2], point)