import numpy as np


def whichfacepoint(U0, a, b, c, point):
    U0 = np.array(U0)
    a = np.array([a, 0, 0])
    b = np.array([0, b, 0])
    c = np.array([0, 0, c])
    vertex = np.array(point)
    distancia = tuple()
    vectornomal = [[1, 0, 0],
                   [0, 1, 0],
                   [0, 0, 1],
                   [-1, 0, 0],
                   [0, -1, 0],
                   [0, 0, -1]]

    faces = [[U0, U0 + a, U0 + a + b, U0 + b],
             [U0 + b, U0 + a + b, U0 + a + b + c, U0 + b + c],
             [U0 + b + c, U0 + a + b + c, U0 + c + a, U0 + c],
             [U0 + c, U0 + c + a, U0 + a, U0],
             [U0, U0 + b, U0 + c, U0 + b + c],
             [U0 + a, U0 + a + b, U0 + a + c, U0 + a + b + c]]
    distancia1 = (((vectornomal[0][0] * vertex[0]) + (vectornomal[0][1] * vertex[1]) + (vectornomal[0][2] * vertex[2])) - (a[0] / 2), "cara frontal")
    distancia2 = (((vectornomal[1][0] * vertex[0]) + (vectornomal[1][1] * vertex[1]) + (vectornomal[1][2] * vertex[2])) - (b[1] / 2), "cara derecha")
    distancia3 = (((vectornomal[2][0] * vertex[0]) + (vectornomal[2][1] * vertex[1]) + (vectornomal[2][2] * vertex[2])) - (c[2] / 2), "cara arriba")
    distancia4 = (((vectornomal[3][0] * vertex[0]) + (vectornomal[3][1] * vertex[1]) + (vectornomal[3][2] * vertex[2])) - (a[0] / 2), "cara atras")
    distancia5 = (((vectornomal[4][0] * vertex[0]) + (vectornomal[4][1] * vertex[1]) + (vectornomal[4][2] * vertex[2])) - (b[1] / 2), "cara izquierda")
    distancia6 = (((vectornomal[5][0] * vertex[0]) + (vectornomal[5][1] * vertex[1]) + (vectornomal[5][2] * vertex[2])) - (c[2] / 2), "cara abajo")
    print(distancia1, "\n", distancia2, "\n", distancia3, "\n", distancia4, "\n", distancia5, "\n", distancia6)

    valorabsoluto = np.zeros([6, 1])
    raiz = np.zeros([6, 1])





if __name__ == '__main__':
    U0 = [5, 4, 6]
    size = [15, 20, 10]
    point = [1, 2, 7]
    whichfacepoint(U0, size[0], size[1], size[2], point)