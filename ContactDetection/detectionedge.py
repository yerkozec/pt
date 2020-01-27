import numpy as np


def edge_detection(U0, a, b, c, Vj, Vk):
    S = np.zeros([3, 2])
    U0 = np.asarray(U0)
    Vj = np.asarray(Vj)
    Vk = np.asarray(Vk)
    Vjprima = Vj - U0
    Vkprima = Vk - U0
    size = [a + U0[0], b + U0[1], c + U0[2]]
    Ro = np.array([[0, a],
                   [0, b],
                   [0, c]])
    W = Vkprima - Vjprima
    Wbool = [False, False, False]
    for i in range(0, 3):
        if -0.0000000001 < W[i] < 0.0000000001:
            Wbool[i] = True
    if Wbool[0] and Wbool[1] or Wbool[0] and Wbool[2] or Wbool[1] and Wbool[2]:
        Sd = Sdetectionwithtwocero(Ro, Vjprima, W)
        inside = paralleltwoedge(U0, size, Vj, W)
        if inside:
            Si, Sf = calSlimit(Sd, Vjprima, Vkprima, U0)
            return Si, Sf, True
        else:
            return Vj, Vk, False
    elif Wbool[0] or Wbool[1] or Wbool[2]:
        inside = paralleledge(U0, size, Vj, W)
        S2d = Sdetectionwithonecero(Ro, Vjprima, W)
        if inside:
            if intersectionanalysis(S2d):
                Si, Sf = calSlimit(S2d, Vjprima, Vkprima, U0)
                return Si, Sf, True
            else:
                return Vj, Vk, False
        else:
            '''print("Arista NO esta en contacto con el poliedro con W = 0")'''
            return Vj, Vk, False
    else:
        S = calcularS(Ro, Vjprima, W, S)
        inside = intersectionanalysis(S)
        if inside:
            Si, Sf = calSlimit(S, Vjprima, Vkprima, U0)
            '''print("Arista se encontro dentro del poliedro")'''
            return Si, Sf, True
        else:
            '''print("Arista NO se esta en contacto")'''
            return Vj, Vk, False


def calcularS(Ro, Vjprima, W, S):
    for i in range(0, 3):
        try:
            S[i] = (Ro[i] - Vjprima[i]) / W[i]
        except (ZeroDivisionError):
            '''print("Se intento dividir por cero")'''
            S[i] = 0
    S = np.sort(S)
    return S


def calcularS2d(Ro, Vjprima, W):
    S = (Ro - Vjprima)/W
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
        '''print("Estoy entre el intervalo de S1 y S2 por la derecha")'''
        if c2 >= d2 >= c1 >= d1:
            '''print("Existe la interseccion de los 3 intervalos por la derecha")'''
            return isinsidedetection(S)
        elif c1 <= d1 <= c2 <= d2:
            '''print("Existe la interseccion de los 3 intervalos por la izq")'''
            return isinsidedetection(S)
        elif d1 <= c1 <= d2 and d1 <= c2 <= d2:
            '''print("Existe la intereccion de los 3 intevalos por el centro")'''
            return isinsidedetection(S)
        elif c1 <= d1 and d2 <= c2:
            '''print("Existe la intereccion de los 3 intevalos contenido por el centro")'''
            return isinsidedetection(S)

    elif a1 <= b2 <= a2 and b1 <= a1:
        d1, d2 = a1, b2
        '''print("Estoy entre el intervalo de S1 y S2 por la izq")'''
        if c2 >= d2 >= c1 >= d1:
            '''print("Existe la interseccion de los 3 intervalos por la derecha")'''
            return isinsidedetection(S)
        elif c1 <= d1 <= c2 <= d2:
            '''print("Existe la interseccion de los 3 intervalos por la izq")'''
            return isinsidedetection(S)
        elif d1 <= c1 <= d2 and d1 <= c2 <= d2:
            '''print("Existe la intereccion de los 3 intevalos por el centro")'''
            return isinsidedetection(S)
        elif c1 <= d1 and d2 <= c2:
            '''print("Existe la intereccion de los 3 intevalos contenido por el centro")'''
            return isinsidedetection(S)

    elif a2 >= b1 >= a1 and a1 <= b2 <= a2:
        d1, d2 = b1, b2
        '''print("Estoy entre el intervalo de S1 y S2 por el centro")'''
        if c2 >= d2 >= c1 >= d1:
            '''print("Existe la interseccion de los 3 intervalos por la derecha")'''
            return isinsidedetection(S)
        elif c1 <= d1 <= c2 <= d2:
            '''print("Existe la interseccion de los 3 intervalos por la izq")'''
            return isinsidedetection(S)
        elif d1 <= c1 <= d2 and d1 <= c2 <= d2:
            '''print("Existe la intereccion de los 3 intevalos por el centro")'''
            return isinsidedetection(S)
        elif c1 <= d1 and d2 <= c2:
            '''print("Existe la intereccion de los 3 intevalos contenido por el centro")'''
            return isinsidedetection(S)

    elif b1 <= a1 and a2 <= b2:
        d1, d2 = a1, a2
        '''print("el segmentso S1 esta contenido en el S2 por el centro")'''
        if c2 >= d2 >= c1 >= d1:
            '''print("Existe la interseccion de los 3 intervalos por la derecha")'''
            return isinsidedetection(S)
        elif c1 <= d1 <= c2 <= d2:
            '''print("Existe la interseccion de los 3 intervalos por la izq")'''
            return isinsidedetection(S)
        elif d1 <= c1 <= d2 and d1 <= c2 <= d2:
            '''print("Existe la intereccion de los 3 intevalos por el centro")'''
            return isinsidedetection(S)
        elif c1 <= d1 and d2 <= c2:
            '''print("Existe la intereccion de los 3 intevalos contenido por el centro")'''
            return isinsidedetection(S)

    else:
        '''print("NO se encontro ninguna interseccion")'''
        return False


def isinsidedetection(S):
    for i in range(0, 3):
        if np.all(S[i] < 0) or np.all(S[i] > 1):
            inside = False
        else:
            inside = True
    return inside


def paralleledge(U0, size, Vjprima, W):
    """print("tiene ceros se tiene que identificar que eje se hace cero")"""
    if W[0] == 0:
        '''print("el eje X se volvio cero por ende es paralelo en el eje x")'''
        dentro = inaxes(Vjprima[0], U0[0], size[0])
        if dentro:
            '''print("se encuentra dentro de la figura en el eje x")'''
            return True
        else:
            '''print("La arista se encuentra fuera de la figura")'''
            return False
    elif W[1] == 0:
        '''print("el eje Y se volvio cero por ende es paralelo en el eje y")'''
        dentro = inaxes(Vjprima[1], U0[1], size[1])
        if dentro:
            '''print("se encuentra dentro de la figura en el eje y")'''
            return True
        else:
            '''print("La arista se encuentra fuera de la figura")'''
            return False
    elif W[2] == 0:
        '''print("el eje Z se volvio cero por ende es paralelo en el eje z")'''
        dentro = inaxes(Vjprima[2], U0[2], size[2])
        if dentro:
            '''print("se encuentra dentro de la figura en el eje z")'''
            return True
        else:
            '''print("La arista se encuentra fuera de la figura")'''
            return False


def paralleltwoedge(U0, size, Vjprima, W):
    inbool = False
    if W[0] == 0 and W[1] == 0:
        if U0[0] <= Vjprima[0] <= size[0]:
            if U0[1] <= Vjprima[1] <= size[1]:
                inbool = True
                return inbool
            else:
                inbool = False
                return inbool
        else:
            return inbool
    elif W[1] == 0 and W[2] == 0:
        if U0[1] <= Vjprima[1] <= size[1]:
            if U0[2] <= Vjprima[2] <= size[2]:
                inbool = True
                return inbool
            else:
                inbool = False
                return inbool
        else:
            return inbool
    elif W[2] == 0 and W[0] == 0:
        if U0[2] <= Vjprima[2] <= size[2]:
            if U0[0] <= Vjprima[0] <= size[0]:
                inbool = True
                return inbool
            else:
                inbool = False
                return inbool
        else:
            return inbool


def inaxes(testaxe, U0, size):
    dentro = False
    if U0 <= testaxe <= size:
        dentro = True
        return dentro
    else:
        return dentro


def Sdetectionwithonecero(Ro,Vjprima, W):
    S2d = np.zeros([3, 2])
    if W[0] == 0:
        S2d[1, :] = calcularS2d(Ro[1, :], Vjprima[1], W[1])
        S2d[0, 1] = 1
        S2d[2, :] = calcularS2d(Ro[2, :], Vjprima[2], W[2])
    elif W[1] == 0:
        S2d[0, :] = calcularS2d(Ro[0, :], Vjprima[0], W[0])
        S2d[1, 1] = 1
        S2d[2, :] = calcularS2d(Ro[2, :], Vjprima[2], W[2])
    elif W[2] == 0:
        S2d[1, :] = calcularS2d(Ro[1, :], Vjprima[1], W[1])
        S2d[0, :] = calcularS2d(Ro[0, :], Vjprima[0], W[0])
        S2d[2, 1] = 1
    S2d = np.sort(S2d)
    return S2d


def Sdetectionwithtwocero(Ro,Vjprima, W):
    Sd = np.zeros([3, 2])
    if W[0] == 0 and W[1] == 0:
        Sd[0, 1] = 1
        Sd[1, 1] = 1
        Sd[2, :] = calcularS2d(Ro[2, :], Vjprima[2], W[2])
    elif W[1] == 0 and W[2] == 0:
        Sd[0, :] = calcularS2d(Ro[0, :], Vjprima[0], W[0])
        Sd[1, 1] = 1
        Sd[2, 1] = 1
    elif W[2] == 0 and W[0] == 0:
        Sd[0, 1] = 1
        Sd[1, :] = calcularS2d(Ro[1, :], Vjprima[1], W[1])
        Sd[2, 1] = 1
    Sd = np.sort(Sd)
    return Sd

