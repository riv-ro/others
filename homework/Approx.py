import time
import numpy as np
from pandas import DataFrame

def approx():
    # N = int(input('n: '))
    # W = int(input('W: '))
    # w = list(map(int, input('w: ').split()))
    # v = list(map(int, input('v: ').split()))

    w = [2,2,1,3,4,2,5,7,7,5,3,3,1,7,5,9,4,9]
    v = [4,5,2,8,3,5,6,7,3,6,2,6,7,6,1,9,6,5]
    N = len(w)
    W = 30

    print('input------')
    print(N)
    print(W)
    print(w)
    print(v)
    print('-----------')

    #評価値の計算
    evaluates = v/w
    #降順にソート(大→小)
    #昇順にソートしてから逆順にする
    evaluates.sort()
    evaluates.reverse()




if __name__ == '__main__':

    #(1+ε)近似アルゴリズムの実装
    start = time.time()
    approx()
    elapsed_time = time.time() -start
    print('elapsed_time:{0}'.format(elapsed_time) + '[sec]')
