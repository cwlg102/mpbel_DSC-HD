#load1 -> load2
import time
import numpy as np
from scipy.spatial import distance
from scipy.spatial.distance import directed_hausdorff
load1 = np.load('vol1_surf.npy') * 1
load2 = np.load('vol2_surf.npy') * 1
intersec = load1 * load2
load1 = load1 - intersec


p1 = np.where(load1==1)
p2 = np.where(load2==1)
print(len(p1[0]))
arr1 = np.zeros([len(p1[0]), 3])
arr2 = np.zeros([len(p2[0]), 3])

for i in range(len(p1[0])):
    arr1[i][0] = p1[0][i]
    arr1[i][1] = p1[1][i]
    arr1[i][2] = p1[2][i]
for i in range(len(p2[0])):
    arr2[i][0] = p2[0][i]
    arr2[i][1] = p2[1][i]
    arr2[i][2] = p2[2][i]


#결과가 같음을 확인...
start = time.time()
res = []
dmax = 0
pointABminimum = [] #95%를 구하기위한....
for i in range(len(arr1)):
    a = arr1[i]
    dmin = 10**8
    for j in range(len(arr2)):
        b = arr2[j]
        dist = np.linalg.norm(a-b)
        if dmin > dist:
            dmin = dist
        if dmax > dist :
            break
    pointABminimum.append(dmin)
    if dmax < dmin:
        dmax = dmin
realhd = max(pointABminimum)
for i in range(len(pointABminimum)):
    if pointABminimum[i] > (0.95 * realhd):
        pointABminimum[i] = 0

print('상위5%:',max(pointABminimum))
print('실제 HD값:', dmax) 
print('시간', time.time()-start)    

#33.4575초 -np.linalg.norm(a-b)
#41.74초 -distance.euclidean(a, b)
#겹치는거 다빼면 8.314초
start = time.time()
print(directed_hausdorff(arr1, arr2)[0])
print('시간', time.time()-start)