import time
import numpy as np
from scipy.spatial import distance
from scipy.spatial.distance import directed_hausdorff
loaded1 = np.load('vol1.npy')
loaded2 = np.load('vol2.npy')
start = time.time()
intersection = loaded1 * loaded2 #아이디어 => 둘의 스칼라곱 하면(행렬곱 No) True*True == True이므로 , 같은 True값 거르기 가능
res = 0
res1 = 0
res2 = 0
###############for문 더 줄이는 법###################
#n=intersection[intersection==True] #intersection안에서 True인것들만 뽑아서 1차원화
#print(np.shape(n))
#################################################
# res = intersection[intersection == True]
# res1 = loaded1[loaded1 == True]
# res2 = loaded2[loaded2 == True]
#np.where함수 -> 0행 -> 0축 1행 -> 1축 ... n행 -> n축 으로 담아냄
res = np.where(intersection == True)[0]
res1 = np.where(loaded1 == True)[0]
res2 = np.where(loaded2 == True)[0]

print('me', 2*len(res)/(len(res1)+len(res2)))
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
