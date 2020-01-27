import numpy as np
import random

def gendata(datarandom):
    if datarandom == "True":
        U0 = 5, 4, 6
        size = 10, 15, 16
        point = list(random.sample(range(30), 3))
        Vj = list(random.sample(range(30), 3))
        Vk = list(random.sample(range(30), 3))
        while Vj == Vk:
            Vk = list(random.sample(range(30), 3))
        return U0, size, point, Vj, Vk
    else:
        U0 = input()
        size = input()
        point = input()
        Vj = input()
        Vk = input()
        posv = input()

        U0 = list(map(float, U0.strip().split()))
        a, b, c = list(map(float, size.strip().split()))
        point = list(map(float, point.strip().split()))
        Vj = list(map(float, Vj.strip().split()))
        Vk = list(map(float, Vk.strip().split()))
        posv = list(map(float, posv.strip().split()))
        return U0, a, b, c, point, Vj, Vk, posv
