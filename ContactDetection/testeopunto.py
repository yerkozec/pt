import datagenerator
import planocartesiano
import detectionvertex
import random
import matplotlib.pyplot as plt
import time
import numpy as np


def testdetection(N):
    countpointin, countpointout, countaristain, countaristaout = 0, 0, 0, 0
    vertextest = np.zeros([N, 3])
    vertexinside = np.zeros([N, 1])
    #------------------ calcular tiempo para punto------------------------

    start_time_point = time.time()
    for i in range(0, N):
        point = list(random.sample(range(30), 3))
        pointinside = detectionvertex.pointdetection(U0, a, b, c, point)
        vertextest[i] = point
        vertexinside[i] = pointinside
        if pointinside:
            countpointin = countpointin + 1
        else:
            countpointout = countpointout + 1

    elapsed_time_point = (time.time() - start_time_point)

    print("tiempo de deteccion de punto:", elapsed_time_point,
          "\nnumero de puntos detectados dentro: ", countpointin,
          "\nnumero de puntos detectados fuera: ", countpointout,
          "\nvectores", vertextest)
    return vertexinside, vertextest


if __name__ == '__main__':
    print("usar datos random para generar figura y pruebas(True/False)?")
    userandom = input()
    if userandom == "True":
        print("cuantas pruebas?")
        ntest = input()
        ntest = int(ntest)
        U0, size, point, Vj, Vk = datagenerator.gendata(userandom)
        a = size[0]
        b = size[1]
        c = size[2]
        pointinside, point = testdetection(ntest)
        ax = planocartesiano.configplano()
        planocartesiano.createfigureplot(ax, U0, a, b, c)
        for i in range(0, ntest):
            planocartesiano.plottestpoint(ax, pointinside[i], point[i])
        plt.show()
    else:
        print(userandom)
        U0, a, b, c, point, Vj, Vk = datagenerator.gendata(userandom)
        pointinside = detectionvertex.pointdetection(U0, a, b, c, point)
        ax = planocartesiano.configplano()
        planocartesiano.createfigureplot(ax, U0, a, b, c)
        planocartesiano.plottestpoint(ax, pointinside, point)
        plt.show()

