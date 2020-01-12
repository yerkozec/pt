import numpy as np


def aristadetection(U0, a, b, c, Vj, Vk):
    S = np.zeros([3, 2])
    U0 = np.asarray(U0)
    Vj = np.asarray(Vj)
    Vk = np.asarray(Vk)
    Vjprima = Vj - U0
    Vkprima = Vk - U0
    size = [a, b, c]
    Ro = np.array([[0, a],
                   [0, b],
                   [0, c]])
    W = Vkprima - Vjprima
    for i in range(0, 3):
        if -0.0000000001 < W[i] < 0.0000000001:
            inside = paralleledge(U0, size, Vjprima, W)
            if inside:
                S = calS(Ro, Vjprima, W, S)
                inside = intersectionanalysis(S)
                if inside:
                    Si, Sf = calSlimit(S, Vjprima, Vkprima, U0)
                    print("arista esta en contacto con el poliedro con W = 0")
                    return Si, Sf, True
            else:
                print("arista NO esta en contacto con el poliedro con W = 0")
                return Vj, Vk, False
        else:
            S = calS(Ro, Vjprima, W, S)
            inside = intersectionanalysis(S)
            if inside:
                Si, Sf = calSlimit(S, Vjprima, Vkprima, U0)
                print("Arista se encontro dentro del poliedro")
                return Si, Sf, True
            else:
                print("Arista NO se esta en contacto")
                return Vj, Vk, False


def calS(Ro, Vjprima, W, S):
    for i in range(0, 3):
        try:
            S[i] = (Ro[i] - Vjprima[i]) / W[i]
        except (ZeroDivisionError):
            print("Se intento dividir por cero")
            S[i] = 0
    S = np.sort(S)
    return S


def calSlimit(S, Vjprima, Vkprima, U0):
    for i in range(0, 3):
        if S[i][0] <= 0:
            S[i][0] = 0
        if S[i][1] >= 1:
            S[i][1] = 1
    Si = np.max(S[:, 0])
    Sf = np.min(S[:, 1])
    Si = (Vjprima + Si * (Vkprima - Vjprima)) + U0
    Sf = (Vjprima + Sf * (Vkprima - Vjprima)) + U0
    return Si, Sf


def intersectionanalysis(S):
    a1, a2, b1, b2, c1, c2 = np.min(S[0, :]), np.max(S[0, :]), np.min(S[1, :]), np.max(S[1, :]), np.min(S[2, :]), np.max(S[2, :]),
    if b2 >= a2 >= b1 >= a1:
        d1, d2 = b1, a2
        print("Estoy entre el intervalo de S1 y S2 por la derecha")
        if c2 >= d2 >= c1 >= d1:
            print("Existe la interseccion de los 3 intervalos por la derecha")
            return isinsidedetection(S)
        elif c1 <= d1 <= c2 <= d2:
            print("Existe la interseccion de los 3 intervalos por la izq")
            return isinsidedetection(S)
        elif d1 <= c1 <= d2 and d1 <= c2 <= d2:
            print("Existe la intereccion de los 3 intevalos por el centro")
            return isinsidedetection(S)
        elif c1 <= d1 and d2 <= c2:
            print("Existe la intereccion de los 3 intevalos contenido por el centro")
            return isinsidedetection(S)

    elif a1 <= b2 <= a2 and b2 <= a2:
        d1, d2 = a1, b2
        print("Estoy entre el intervalo de S1 y S2 por la izq")
        if c2 >= d2 >= c1 >= d1:
            print("Existe la interseccion de los 3 intervalos por la derecha")
            return isinsidedetection(S)
        elif c1 <= d1 <= c2 <= d2:
            print("Existe la interseccion de los 3 intervalos por la izq")
            return isinsidedetection(S)
        elif d1 <= c1 <= d2 and d1 <= c2 <= d2:
            print("Existe la intereccion de los 3 intevalos por el centro")
            return isinsidedetection(S)
        elif c1 <= d1 and d2 <= c2:
            print("Existe la intereccion de los 3 intevalos contenido por el centro")
            return isinsidedetection(S)

    elif a2 >= b1 >= a1 and a1 <= b2 <= a2:
        d1, d2 = b1, b2
        print("Estoy entre el intervalo de S1 y S2 por el centro")
        if c2 >= d2 >= c1 >= d1:
            print("Existe la interseccion de los 3 intervalos por la derecha")
            return isinsidedetection(S)
        elif c1 <= d1 <= c2 <= d2:
            print("Existe la interseccion de los 3 intervalos por la izq")
            return isinsidedetection(S)
        elif d1 <= c1 <= d2 and d1 <= c2 <= d2:
            print("Existe la intereccion de los 3 intevalos por el centro")
            return isinsidedetection(S)
        elif c1 <= d1 and d2 <= c2:
            print("Existe la intereccion de los 3 intevalos contenido por el centro")
            return isinsidedetection(S)

    elif b1 <= a1 and a2 <= b2:
        d1, d2 = a1, a2
        print("el segmentso S1 esta contenido en el S2 por el centro")
        if c2 >= d2 >= c1 >= d1:
            print("Existe la interseccion de los 3 intervalos por la derecha")
            return isinsidedetection(S)
        elif c1 <= d1 <= c2 <= d2:
            print("Existe la interseccion de los 3 intervalos por la izq")
            return isinsidedetection(S)
        elif d1 <= c1 <= d2 and d1 <= c2 <= d2:
            print("Existe la intereccion de los 3 intevalos por el centro")
            return isinsidedetection(S)
        elif c1 <= d1 and d2 <= c2:
            print("Existe la intereccion de los 3 intevalos contenido por el centro")
            return isinsidedetection(S)

    else:
        print("NO se encontro ninguna interseccion")
        return False


def isinsidedetection(S):
    for i in range(0, 3):
        if np.all(S[i] < 0) or np.all(S[i] > 1):
            inside = False
        else:
            inside = True
    return inside


def paralleledge(U0, size, Vjprima, W):
    print("tiene ceros se tiene que identificar que eje se hace cero")
    if W[0] == 0:
        print("el eje X se volvio cero por ende es paralelo en el eje x")
        if inaxes(Vjprima[0], U0[0], size[0]):
            print("se encuentra dentro de la figura en el eje x")
            return True
        else:
            print("La arista se encuentra fuera de la figura")
            return False
    elif W[1] == 0:
        print("el eje Y se volvio cero por ende es paralelo en el eje y")
        if inaxes(Vjprima[1], U0[1], size[1]):
            print("se encuentra dentro de la figura en el eje y")
            return True
        else:
            print("La arista se encuentra fuera de la figura")
            return False
    else:
        print("el eje Z se volvio cero por ende es paralelo en el eje z")
        if inaxes(Vjprima[2], U0[2], size[2]):
            print("se encuentra dentro de la figura en el eje z")
            return True
        else:
            print("La arista se encuentra fuera de la figura")
            return False


def inaxes(testaxe, U0, size):
    if U0 < testaxe < size:
        return True
    else:
        return False


'''
def whichfacepoint(U0, a, b, c, point):
    U0 = np.array(U0)
    a = np.array([a, 0, 0])
    b = np.array([0, b, 0])
    c = np.array([0, 0, c])
    faces = [[U0, U0 + a, U0 + a + b, U0 + b],
             [U0 + b, U0 + a + b, U0 + a + b + c, U0 + b + c],
             [U0 + b + c, U0 + a + b + c, U0 + c + a, U0 + c],
             [U0 + c, U0 + c + a, U0 + a, U0],
             [U0, U0 + b, U0 + c, U0 + b + c],
             [U0 + a, U0 + a + b, U0 + a + c, U0 + a + b + c]]
    vectornormales = genvectornormal(faces, point)
    valorabsoluto = np.zeros([6, 1])
    raiz = np.zeros([6, 1])
    distancias = np.zeros([6, 2])
    for i in range(0, 6):
        valorabsoluto[i] = (abs((vectornormales[i][0] + point[0]) + (vectornormales[i][1] + point[1]) + (vectornormales[i][2] + point[2]) + (a[0])))
        raiz[i] = (np.sqrt((vectornormales[i][0] ** 2) + (vectornormales[i][1] ** 2) + (vectornormales[i][2] ** 2)))
        distancias[i] = ((valorabsoluto[i] / raiz[i]), i)
    print(distancias)
    np.sort(distancias)


def genvectornormal(faces, point):
    prodmix = np.zeros([6, 2])
    prodmix = ([1, 0, 0],
               [0, 1, 0],
               [-1, 0, 0],
               [0, -1, 0],
               [0, 0, 1],
               [0, 0, -1])
    return prodmix
    
    
  print("\nU0:", U0,
   "\n a:", a, "\nb:",
    b,"\nVj:", Vj, "\nVk:", Vk, "\n Vj*:", Vjprima, "\n Vk*:", Vkprima, "\nW:", W, "\n Ro:", Ro)


        print("Ro: ", Ro[i], "\nVjprima:", Vjprima[i], "\nW:", W[i])
        print("ro - vjprima", Ro[i] - Vjprima[i])
        print("SS:", S[i], "\nSe termina el loop \n")
    print("\nS antes de sort: \n", S)



    inside = insidedetection(S)

    print("\nS despues de sort: \n", S)



    if (inside):
        return Si, Sf, True


    else:
        return Vj, Vk, False
    Si = np.array([[s[0][0] - Vj[0]],
                   [s[1][0] - Vj[1]],
                   [s[2][0] - Vj[2]]])
    print("s:\n", Si, "\n y J:\n ", J)

    if not J[0][0] or not J[1][0] or not J[2][0]:
        if not J[0][1] or not J[1][1] or not J[2][1]:
            return J, False, s, Vjprima, Vkprima
        else:
            if not J[0][0]:
                J[0][0] = a
            if not J[1][0]:
                J[1][0] = b
            if not J[2][0]:
                J[2][0] = c
            return J, True, s, Vjprima, Vkprima
    if not J[0][1] or not J[1][1] or not J[2][1]:
        if not J[0][0] or not J[1][0] or not J[2][0]:
            return J, False, s, Vjprima, Vkprima
        else:
            if not J[0][1]:
                J[0][1] = a
            if not J[1][1]:
                J[1][1] = b
            if not J[2][1]:
                J[2][1] = c
            return J, True, s, Vjprima, Vkprima
    else:
        return J, True, s, Vjprima, Vkprima

'''
