import datagenerator
import planocartesiano
import detection3d
import random
import matplotlib.pyplot as plt
import time


def testdetection():
    countpointin, countpointout, countaristain, countaristaout = 0, 0, 0, 0

    #------------------ calcular tiempo para punto------------------------

    start_time_point = time.time()
    for i in range(0, 10):
        point = list(random.sample(range(30), 3))
        pointinside = detection3d.pointdetection(U0, a, b, c, point)
        if pointinside:
            countpointin = countpointin + 1
        else:
            countpointout = countpointout + 1
        i = i + 1
    elapsed_time_point = (time.time() - start_time_point)

    #------------------calcular tiempo para arista-------------------------
    start_time_arista = time.time()
    for j in range(0, 10):
        Vj = list(random.sample(range(30), 3))
        Vk = list(random.sample(range(30), 3))
        Si, Sf, aristainside = detection3d.aristadetection(U0, a, b, c, Vj, Vk)
        if aristainside:
            countaristain = countaristain + 1
        else:
            countaristaout = countaristaout + 1
        j = j + 1

    elapsed_time_arista = (time.time() - start_time_arista)
    print("tiempo de deteccion de punto:", elapsed_time_point,
          "\ntiempo de deteccion de arista: ", elapsed_time_arista,
          "\nnumero de aristas detectadas dentro: ", countaristain,
          "\nnumero de aristas detectadas fuera: ", countaristaout,
          "\nnumero de puntos detectados dentro: ", countpointin,
          "\nnumero de puntos detectados fuera: ",countpointout)
    return pointinside, point, Si, Sf, aristainside, Vj, Vk

if __name__ == '__main__':
    print("usar datos random para generar figura y pruebas(True/False)?")
    userandom = input()
    if userandom == "True":
        U0, size, point, Vj, Vk = datagenerator.gendata(userandom)
        a = size[0]
        b = size[1]
        c = size[2]
    else:
        U0, a, b, c, point, Vj, Vk = datagenerator.gendata(userandom)

    '''pointinside = detection3d.pointdetection(U0, a, b, c, point)
    Si, Sf, aristainside = detection3d.aristadetection(U0, a, b, c, Vj, Vk)'''
    pointinside, point, Si, Sf, aristainside, Vj, Vk = testdetection()

    ax = planocartesiano.configplano()
    planocartesiano.createfigureplot(ax, U0, a, b, c)
    planocartesiano.plottestpoint(ax, pointinside, point)
    planocartesiano.plottestarista(ax, Si, Sf, aristainside, Vj, Vk)
    plt.show()


'''Si, Sf, pointinside, aristainside, Vj, Vk, point =  testdetection()
U0 = [2, 4, 2]
a, b, c = 10, 15, 25

print("U0: ", U0, "\nsize: ", size, "\npoint: ", point, "\nVj: ", Vj, "\nVk: ", Vk)
whichfacepoint(U0, a, b, c, point)
Si, Sf, aristainside = aristadetection(U0, a, b, c, Vj, Vk)
pointinside = pointdetection(U0, a, b, c, point)
'''