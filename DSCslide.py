import time
import numpy as np
from scipy.spatial import distance
from scipy.spatial.distance import directed_hausdorff

def DicebyChan():
    loaded1 = np.load('vol1.npy')
    loaded2 = np.load('vol2.npy')
    
    intersection = loaded1 * loaded2 #아이디어 => 둘의 스칼라곱 하면(행렬곱 No) True*True == True이므로 , 같은 True값 거르기 가능

    
    result = []
    for k in range(len(loaded1)):
        if np.all(loaded1[k] == False) or np.all(loaded2[k] == False):
            result.append(0)
            continue
        gyojiphap_length = len(np.where(intersection[k]==True)[0]) * 2
        hapjiphap_length = len(np.where(loaded1[k] == True)[0]) + len(np.where(loaded2[k] == True)[0])
        result.append(gyojiphap_length/hapjiphap_length)

    print(max(result))
    
def DicebyFunc():
    loaded1 = np.load('vol1.npy')
    loaded2 = np.load('vol2.npy')
    rstfunc = []
    for k in range(len(loaded1)):
        if np.all(loaded1[k] == False) or np.all(loaded2[k] == False):
            rstfunc.append(0)
            continue
        l11dim = np.ravel(loaded1[k])
        l21dim = np.ravel(loaded2[k])

        val = distance.dice(l11dim, l21dim)
        rstfunc.append(1-val)

    print(max(rstfunc))

start = time.time()
DicebyChan()
a = time.time()-start
print('시간:', a)

start = time.time()
DicebyFunc()
b = time.time()-start
print('시간:', b)

if a < b:print('승리')
else:print('패배')