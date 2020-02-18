import matplotlib.pyplot as plt
import numpy as np
from pylab import *

N = 5
axesX = [100, 1000, 10000, 50000]
axesY = [0.00311422348, 0.02841091156, 0.29450845718, 1.4508020877838]
tiempo = np.zeros([5, 1])
axesXpendiente = [0, 50000]
axesYpendiente = [0, 2]
axesXX = [100, 1000, 10000, 50000]
axesYY = [0.039597749, 0.14173412322, 1.13699746131, 5.3653037548065]
#axesYYpendiente = [axesX[1]**2, axesX[2]**2, axesX[3]**2, axesX[4]**2]
x = arange(50000.)



def graficarvertice():
    plt.loglog(axesX, axesY, '-ro')
    xx = [100, 1000, 10000, 50000]
    yy = [100, 1000, 10000, 50000]
    yyy = [100 ** 2, 1000 ** 2, 10000 ** 2, 50000 ** 2]
    plt.loglog(xx, yy, '-bo')
    plt.loglog(xx, yyy, '-go')
    plt.xlabel('N cantidad de vértices')
    plt.ylabel('Tiempo en segundos')
    plt.title('Tiempo vs N vértices')
    plt.grid()
    plt.show()

def graficararista():
    xx = [100, 1000, 10000, 50000]
    yy = [100, 1000, 10000, 50000]
    yyy = [100**2, 1000**2, 10000**2, 50000**2]
    plt.loglog(xx, yy, '-bo')
    plt.loglog(axesXX, axesYY, '-ro')
    plt.loglog(xx, yyy, '-go')
    plt.xlabel('N cantidad de aristas')
    plt.ylabel('Tiempo en segundos')
    plt.title('Tiempo vs N aristas')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    setfile = open("./resultados/tiempovertices.out", "rt")
    print(axesYY[2] - axesYY[1] / axesXX[2] - axesXX[1])
    line1 = setfile.readline()
    line2 = setfile.readline()
    line3 = setfile.readline()
    line4 = setfile.readline()
    line5 = setfile.readline()
    lines = line1 + line2 + line3 + line4 + line5
    for i in range(len(line3)):
        if line3[i] == ':':
            for j in range(i, len(line3)):
                print(line3[j])
    setfile.close()
    graficarvertice()
    graficararista()
