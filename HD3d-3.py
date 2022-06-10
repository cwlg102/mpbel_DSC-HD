#load1 -> load2
import time
import numpy as np
from scipy.spatial import distance
from scipy.spatial.distance import directed_hausdorff
load1 = np.load('vol1_surf.npy') * 1
load2 = np.load('vol2_surf.npy') * 1
#volumedata로 아래와 같이 했다간 다른 결과가 나옴
#surface는 겹치는게 line이고 그 부분을 없애도 HD계산에 영향을 주지 않는 것으로 보임
#volume은 겹치는게 volume이므로 겹치는 부분을없애면 거리 계산에 영향이 있는 것으로 생각됨.
intersec = load1 * load2
load1 = load1 - intersec
#이렇게 하면 시간이 많이 줄어듦

p1 = np.where(load1==1)
p2 = np.where(load2==1)

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
#이렇게 하면 속도 많이줄어듦...
np.random.shuffle(arr1)
np.random.shuffle(arr2)
for i in range(len(arr1)):
    #print('진행상황: ', (i/len(arr1))*100)
    a = arr1[i]
    dmin = 10**8
    flag = 0
    for j in range(len(arr2)):
        b = arr2[j]
        dista = np.linalg.norm(a-b)
        if dmin > dista:
            dmin = dista
        if dmax > dista :
            break
        flag = 1
    
    pointABminimum.append(dmin)
    if dmax < dmin:
        dmax = dmin

realmax = max(pointABminimum)
for i in range(len(pointABminimum)):
    if pointABminimum[i] > (0.95 * realmax):
        pointABminimum[i] = 0

print('상위5%HD:',max(pointABminimum))
print('실제 HD값:', dmax) 
print('시간', time.time()-start)    

#33.4575초 -np.linalg.norm(a-b)
#41.74초 -distance.euclidean(a, b)
#겹치는거 다빼면 8.314초
#random사용 -> 2초대(겹치는것을 둘다 없애면..)
start = time.time()
print('함수 HD값:', directed_hausdorff(arr1, arr2)[0])
print('시간', time.time()-start)