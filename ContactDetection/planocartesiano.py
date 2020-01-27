import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def setplane():
    ax = plt.axes(projection='3d')
    ax.set_xlim3d(0, 30)
    ax.set_ylim3d(0, 30)
    ax.set_zlim3d(0, 30)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    return ax

def plotpoliedron(ax, U0, a, b, c):
    etiquietas = ("U0", "U1", "U2", "U3", "U4", "U5", "U6", "U7")
    labels = (None, None, None, None, None, None, None, None)
    xs = (U0[0], U0[0] + a, U0[0] + a, U0[0]    , U0[0]    , U0[0] + a, U0[0] + a, U0[0]    )
    ys = (U0[1], U0[1]    , U0[1]    , U0[1]    , U0[1] + b, U0[1] + b, U0[1] + b, U0[1] + b)
    zs = (U0[2], U0[2]    , U0[2] + c, U0[2] + c, U0[2]    , U0[2]    , U0[2] + c, U0[2] + c)
    for etiqueta, x, y, z, tag in zip(labels, xs, ys, zs, etiquietas):
        label = '%s' % (tag)
        ax.text(x, y, z, label, etiqueta)

    etiquietas = ("F0", "F1", "F2", "F3", "F4", "F5")
    labels = (None, None, None, None, None, None)
    xs = (U0[0] + a/2, U0[0] + a  , U0[0] + a/2, U0[0]      , U0[0] + a/2, U0[0] + a/2)
    ys = (U0[1]      , U0[1] + b/2, U0[1] + b/2, U0[1] + b/2, U0[1] + b/2, U0[1] + b  )
    zs = (U0[2] + c/2, U0[2] + c/2, U0[2] + c  , U0[2] + c/2, U0[2]      , U0[2] + c/2)
    for etiqueta, x, y, z, tag in zip(labels, xs, ys, zs, etiquietas):
        label = '%s' % (tag)
        ax.text(x, y, z, label, etiqueta)

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


def plotvertex(ax, inside, point):
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


def plotedge(ax, Si, Sf, inside, Vj, Vk, puntointerseccion):
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
        ax.plot3D((puntointerseccion[0], puntointerseccion[0]),
                  (puntointerseccion[1], puntointerseccion[1]),
                  (puntointerseccion[2], puntointerseccion[2]),
                  'o',
                  color='m')
    else:
        ax.plot3D((Vj[0], Vk[0]),
                  (Vj[1], Vk[1]),
                  (Vj[2], Vk[2]),
                  'o-',
                  color='r')
