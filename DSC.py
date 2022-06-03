import time
import numpy as np
from scipy.spatial import distance
from scipy.spatial.distance import directed_hausdorff
loaded1 = np.load('vol1.npy')
loaded2 = np.load('vol2.npy')
intersection = 0
section1 = 0
section2 = 0
start = time.time()
for k in range(len(loaded1)):
    for i in range(len(loaded1[k])):
        for j in range(len(loaded1[k][i])):
            if loaded1[k][i][j] == loaded2[k][i][j] and loaded1[k][i][j] == True:
                intersection += 1
            if loaded1[k][i][j] == True:
                section1 += 1
            if loaded2[k][i][j] == True:
                section2 += 1
            
print('3차원배열 포문 돌린거:', (2*intersection)/(section1+section2))
print('시간', time.time()-start)
#1차원으로 만들어 버리기
start = time.time()
l1_1dim = []
l2_1dim = []

for k in range(len(loaded1)):
    for i in range(len(loaded1[k])):
        for j in range(len(loaded1[k][i])):
            l1_1dim.append(loaded1[k][i][j])
            l2_1dim.append(loaded2[k][i][j])
print('함수쓴 값:',1-distance.dice(l1_1dim, l2_1dim))
print('시간', time.time()-start)