import time
import numpy as np
from matplotlib import pyplot as plt
import copy
#https://rfriend.tistory.com/291
label = np.load('w5_label.npy')
pred = np.load('w5_pred.npy')
start = time.time()
threshold = np.linspace(1, 0, 1000)[1: 999]
x = []
y = []
for pivot in threshold:
    predcy = copy.deepcopy(pred)
    predcy[predcy >= pivot] = 1 #불리언 인덱싱, 그리고 값 바꾸기
    predcy[predcy < pivot] = 0
    #print(predcy)
    trueposi = label * predcy
    falseposi = predcy - label
    truenega = label + predcy #에서 0인거
    falsenega = label - predcy #에서 1인거
    
    TP = len(trueposi[trueposi == 1])
    FP = len(falseposi[falseposi == 1])
    TN = len(truenega[truenega == 0])
    FN = len(falsenega[falsenega == 1])
    tpr = TP/(TP+FN)
    fpr = FP/(FP+TN)
    x.append(fpr)
    y.append(tpr)
print(time.time()-start)
plt.plot(x, y)
plt.show()


