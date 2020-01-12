import datagenerator
import planocartesiano
import detectionedge
import random
import matplotlib.pyplot as plt
import time
import numpy as np

def testdetection(N):
    countpointin, countpointout, countaristain, countaristaout = 0, 0, 0, 0
    edgetest = np.zeros([N, 6])
    edgein = np.zeros([N, 1])
    edgesegmentinside = np.zeros([N, 6])
    #------------------calcular tiempo para arista-------------------------
    start_time_arista = time.time()
    for i in range(0, N):
        Vj = list(random.sample(range(30), 3))
        Vk = list(random.sample(range(30), 3))
        Si, Sf, aristainside = detectionedge.aristadetection(U0, a, b, c, Vj, Vk)
        edgetest[i, :3] = Vj[0], Vj[1], Vj[2]
        edgetest[i, 3:] = Vk[0], Vk[1], Vk[2]
        edgein[i] = aristainside
        edgesegmentinside[i, :3] = Si[0], Si[1], Si[2]
        edgesegmentinside[i, 3:] = Sf[0], Sf[1], Sf[2]
        if aristainside:
            countaristain = countaristain + 1
        else:
            countaristaout = countaristaout + 1
        print("-------------TERMINO EL LOOP NUMERO", i, "-----------------------")

    elapsed_time_arista = (time.time() - start_time_arista)
    print("tiempo de deteccion de arista: ", elapsed_time_arista,
          "\nnumero de aristas detectadas dentro: ", countaristain,
          "\nnumero de aristas detectadas fuera: ", countaristaout)

    return edgesegmentinside, edgein, edgetest

if __name__ == '__main__':
    print("usar datos random para generar figura y pruebas(True/False)?")
    userandom = input()
    if userandom == "True":
        print("Cuantas pruebas?")
        ntest = input()
        ntest = int(ntest)
        U0, size, point, Vj, Vk = datagenerator.gendata(userandom)
        a = size[0]
        b = size[1]
        c = size[2]
        edgesegmentin, edgein, edgetest = testdetection(ntest)
        ax = planocartesiano.configplano()
        planocartesiano.createfigureplot(ax, U0, a, b, c)
        for i in range(0, ntest):
            Vj = edgetest[i, 0:3]
            Vk = edgetest[i, 3:6]
            Si = edgesegmentin[i, 0:3]
            Sf = edgesegmentin[i, 3:6]
            planocartesiano.plottestarista(ax, Si, Sf, edgein[i], Vj, Vk)
        plt.show()
    else:
        print(userandom)
        U0, a, b, c, point, Vj, Vk = datagenerator.gendata(userandom)
        Si, Sf, aristainside = detectionedge.aristadetection(U0, a, b, c, Vj, Vk)
        ax = planocartesiano.configplano()
        planocartesiano.createfigureplot(ax, U0, a, b, c)
        planocartesiano.plottestarista(ax, Si, Sf, aristainside, Vj, Vk)
        plt.show()



