import time
import numpy as np
from scipy.spatial import distance
from scipy.spatial.distance import directed_hausdorff
def HausbyChan():
    load1 = np.load('vol1_surf.npy') * 1
    load2 = np.load('vol2_surf.npy') * 1
    result = []

    for k in range(len(load1)):
        insec = load1[k] * load2[k]
        load1[k] -= insec #load1->load2 기준 거리 겹치는거 빼도됨!
        p1 = np.where(load1[k]==1)
        p2 = np.where(load2[k]==1)

        # arr1 = np.transpose(p1) #0.6초대
        # arr2 = np.transpose(p2)

        arr1 = np.zeros([len(p1[0]), 2]) #0.5초대
        arr2 = np.zeros([len(p2[0]), 2])

        for i in range(len(p1[0])):
            arr1[i][0] = p1[0][i]
            arr1[i][1] = p1[1][i]
        for i in range(len(p2[0])):
            arr2[i][0] = p2[0][i]
            arr2[i][1] = p2[1][i]

        if len(arr1) == 0 or len(arr2) == 0:
            continue
        
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
                #최솟값중 최댓값을 구하는것이 Hausdorff Distance.
                #반복을 할때 1->2라고 하면 1번 기하의 한 점에서 2번 기하의 점들을 도는게 안쪽 루프문
                #안쪽 루프를 한번 돌고나면 최솟값이 하나 나옴
                #그리고 (기존의 최솟값들중 최댓값)과 비교하여 크면 업데이트를 하고 아니면 안함
                #안쪽 루프를 돌때, 1번기하의 한점과 2번기하의 임의의 한 점에대한 거리 계산 값이 (기존의 최솟값들 중 최댓값) 보다 작으면 break
                #큰게 나오면 무시할테니깐
                #안쪽 루프는 작을수록 최솟값을 업데이트 하는 구조인데, 그 값보다 더 큰값이 나오지 않을 것이라는게 자명함
                #dmax가 구한 distance보다 클 경우 break을 하면 됨.
                if dmax > dista:
                    break
            if dmin > dmax:
                dmax = dmin

        result.append(dmax)

    print('chan최대:', max(result))
   
    print('chan최소:', min(result))
    
    realmax = max(result)
    for i in range(len(result)):
        if result[i] >= 0.95*realmax:
            result[i] = min(result)
    print('chan 95%:', max(result))
start = time.time()
HausbyChan()
print('시간:', time.time()-start)
print()

def HausbyFunc():
    load1 = np.load('vol1_surf.npy') * 1
    load2 = np.load('vol2_surf.npy') * 1
    resultfunc = []
    for k in range(len(load1)):
        #print('진행상황:', (k/len(load1))*100)
        insec = load1[k] * load2[k]
        load1[k] -= insec #load1->load2 기준 거리 겹치는거 빼도됨!
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

        if len(arr1) == 0 or len(arr2) == 0:
            continue
        resultfunc.append(directed_hausdorff(arr1, arr2)[0])

    print('함수 최대:', max(resultfunc))
    print('함수 최소:', min(resultfunc))

    realmax = max(resultfunc)
    for i in range(len(resultfunc)):
        if resultfunc[i] >= 0.95*realmax:
            resultfunc[i] = min(resultfunc)
    print('함수 95%:', max(resultfunc))

start = time.time()
HausbyFunc()
print('시간:', time.time()-start)