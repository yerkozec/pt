import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def configplano():
    ax = plt.axes(projection='3d')
    ax.set_xlim3d(0, 30)
    ax.set_ylim3d(0, 30)
    ax.set_zlim3d(0, 30)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    return ax

def createfigureplot(ax, U0, a, b, c):
    ax.plot3D((U0[0], U0[0] + a),
              (U0[1], U0[1]),
              (U0[2], U0[2]),
              'o-',
              color='m')
    ax.plot3D((U0[0], U0[0]),
              (U0[1], U0[1] + b),
              (U0[2], U0[2]),
              'o-',
              color='m')
    ax.plot3D((U0[0] + a, U0[0] + a),
              (U0[1], U0[1] + b),
              (U0[2], U0[2]),
              'o-',
              color='m')
    ax.plot3D((U0[0] + a, U0[0]),
              (U0[1] + b, U0[1] + b),
              (U0[2], U0[2]),
              'o-',
              color='m')
    ax.plot3D((U0[0], U0[0] + a),
              (U0[1], U0[1]),
              (U0[2] + c, U0[2] + c),
              'o-',
              color='y')
    ax.plot3D((U0[0], U0[0]),
              (U0[1], U0[1] + b),
              (U0[2] + c, U0[2] + c),
              'o-',
              color='y')
    ax.plot3D((U0[0] + a, U0[0] + a),
              (U0[1], U0[1] + b),
              (U0[2] + c, U0[2] + c),
              'o-',
              color='y')
    ax.plot3D((U0[0] + a, U0[0]),
              (U0[1] + b, U0[1] + b),
              (U0[2] + c, U0[2] + c),
              'o-',
              color='y')
    ax.plot3D((U0[0], U0[0]),
              (U0[1], U0[1]),
              (U0[2], U0[2] + c),
              'o-',
              color='c')
    ax.plot3D((U0[0] + a, U0[0] + a),
              (U0[1], U0[1]),
              (U0[2], U0[2] + c),
              'o-',
              color='c')
    ax.plot3D((U0[0] + a, U0[0] + a),
              (U0[1] + b, U0[1] + b),
              (U0[2], U0[2] + c),
              'o-',
              color='c')
    ax.plot3D((U0[0], U0[0]),
              (U0[1] + b, U0[1] + b),
              (U0[2], U0[2] + c),
              'o-',
              color='c')


# ----------------------------------- plotear arista y punto a estudiar--------------------------
def plottestpoint(ax, inside, point):
    if (inside):
        ax.plot3D((point[0], point[0]),
                  (point[1], point[1]),
                  (point[2], point[2]),
                  'o',
                  color='c')
    else:
        ax.plot3D((point[0], point[0]),
                  (point[1], point[1]),
                  (point[2], point[2]),
                  'o',
                  color='r')


def plottestarista(ax, Si, Sf, inside, Vj, Vk):
    if (inside):
        ax.plot3D((Vj[0], Vk[0]),
                  (Vj[1], Vk[1]),
                  (Vj[2], Vk[2]),
                  'o-',
                  color='b')
        ax.plot3D((Si[0], Sf[0]),
                  (Si[1], Sf[1]),
                  (Si[2], Sf[2]),
                  'o-',
                  color='y')
    else:
        ax.plot3D((Vj[0], Vk[0]),
                  (Vj[1], Vk[1]),
                  (Vj[2], Vk[2]),
                  'o-',
                  color='r')
