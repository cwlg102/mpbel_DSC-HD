import time
import numpy as np
from scipy.spatial import distance
from scipy.spatial.distance import directed_hausdorff
loaded1 = np.load('vol1.npy')
loaded2 = np.load('vol2.npy')
start = time.time()
intersection = loaded1 * loaded2 #아이디어 => 둘의 스칼라값 끼리 곱하면 True*True == True이므로 , 같은 True값 거르기 가능
res = 0
res1 = 0
res2 = 0
for k in range(len(intersection)):
    for i in range(len(intersection[k])):
        res += np.count_nonzero(intersection[k][i] == True)
        res1 += np.count_nonzero(loaded1[k][i] == True) #count_nonzero -> 1차원 벡터에 대해 안에 특정 값이 몇개있는지 검사해준다!!
        res2 += np.count_nonzero(loaded2[k][i] == True)
print('me', 2*res/(res1+res2))
t1 =time.time() - start
print('me시간', t1)


#1차원으로 만들어 버리기
start = time.time()
l1_1dim = np.ravel(loaded1) #ravel 함수는 몇차원 배열이든 1차원으로 펴버림
l2_1dim = np.ravel(loaded2)
print('함수:',1-distance.dice(l1_1dim, l2_1dim))
t2 = time.time() -start
print('함수시간', t2)

if t1 > t2:
    print('패배')
else:print('승리')
