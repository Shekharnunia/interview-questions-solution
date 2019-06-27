import sys
import numpy as np
from itertools import combinations


def solution(array):
    d = []
    for i,v in enumerate(array):
        d.append(np.where(array == v)[0])

    l = []
    for i in d:
        if len(i) <= 1:
            pass
        elif len(i) ==2:
            l.extend(list(combinations(i, 2)))
            
        else:
            l.extend(list(combinations(i, 2)))

    if len(set(l))>0:
       return len(set(l)), set(l)
    else:
        return 0


a = input('Enter value using a coma : ')
array = [int(i) if int(i)<1000000000 and int(i)>-1000000000 else sys.exit('Give value between 1000000000 and -1000000000') for i in a.split(',')]
# array = [int(i) for i in a.split(',')]
array = np.array(array)
sys.exit('Limit crossed of input values') if len(array)>10 else print(solution(array))
