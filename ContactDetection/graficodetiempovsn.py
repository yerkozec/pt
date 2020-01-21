import matplotlib.pyplot as plt
import numpy as np

N = 5
axesX = [0, 100, 1000, 10000, 50000]
axesY = [0, 0.00311422348, 0.02841091156, 0.29450845718, 1.4508020877838]
tiempo = np.zeros([5, 1])

def graficar():
    plt.plot(axesX, axesY, '-o')
    plt.xlabel('N cantidad de vertices')
    plt.ylabel('Tiempo en segundos')
    plt.title('Tiempo vs N vectores')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    setfile = open("./resultados/tiempovertices.out", "rt")
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
    graficar()
