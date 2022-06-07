import time
import numpy as np
from scipy.spatial import distance
from scipy.spatial.distance import directed_hausdorff
load1 = np.load('vol1_surf.npy') * 1
load2 = np.load('vol2_surf.npy') * 1

result = []
resultfunc = []
for k in range(len(load1)):
    p1 = np.where(load1[k]==1)
    p2 = np.where(load2[k]==1)
    arr1 = np.zeros([len(p1[0]), 2])
    arr2 = np.zeros([len(p2[0]), 2])

    for i in range(len(p1[0])):
        arr1[i][0] = p1[0][i]
        arr1[i][1] = p1[1][i]
    for i in range(len(p2[0])):
        arr2[i][0] = p2[0][i]
        arr2[i][1] = p2[1][i]

    np.random.shuffle(arr1)
    np.random.shuffle(arr2)
    dmax = 0
    for i in range(len(arr1)):
        dmin = 10000
        a = arr1[i]
        for j in range(len(arr2)):
            b = arr2[j]
            dista = np.linalg.norm(a - b)
            if dmin > dista:
                dmin = dista
            if dmax > dista:
                break
        if dmin > dmax:
            dmax = dmin
    
    result.append(dmax)
    resultfunc.append(directed_hausdorff(arr1, arr2)[0])

print(result)
print(max(result))
print(min(result))
print(resultfunc)
print(max(resultfunc))
print(min(resultfunc))






