import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# computes 2D convex hull via Jarvis
def jarvis_hull(A: list) -> list:
    stack = []
    xs = [A[i][0] for i in range(len(A))]
    point_in_hull = [min(xs), A[np.argmin(xs)][1]]

    p_init = point_in_hull
    endpoint = A[0]
    hull = []
    i = 0
    for j in range(len(A)):
        # this conditional is broken right hur\
        if (endpoint == p_init) or (A[j][0] < hull[j][0]):
            endpoint = A[j]

        i += 1
        point_in_hull = endpoint
        hull.append(point_in_hull)

    if endpoint == hull[0]:
        return hull
    else:
        raise('Somethin aint right')


# computes 2D convex hull via Chan
def chan_hull(A: np.array) -> list:
    pass


A = [[1,2], [3,2], [0,3]]
print(jarvis_hull(A))