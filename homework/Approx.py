import time
import numpy as np
from pandas import DataFrame

def approx():
    # N = int(input('n: '))
    # W = int(input('W: '))
    # w = list(map(int, input('w: ').split()))
    # v = list(map(int, input('v: ').split()))

    # w = np.array([2,2,1,3,4,2,5,7,7,5,3,3,1,7,5,9,4,9])
    # v = np.array([4,5,2,8,3,5,6,7,3,6,2,6,7,6,1,9,6,5])
    # N = len(w)
    # W = 30

    w = np.load('./npy/weight_750.npy')
    v = np.load('./npy/value_750.npy')
    N = len(w)
    W = 30

    # xの配列。初期値はすべて0とする。採択した時に1にする。
    results = np.zeros(N)

    print('input------')
    print(N)
    print(W)
    print(w)
    print(v)
    print('-----------')

    #評価値の計算
    evaluates = v/w

    # DataFrameにまとめる
    target_df = DataFrame(np.c_[evaluates, w, v, results])
    target_df.index = np.arange(N)
    target_df.columns = ['evaluate', 'weight', 'value', 'result']
    # evaluateの値で降順に並び替える
    target_df = target_df.sort_values(by='evaluate', ascending=False)

    # 採択した項目のweightの和。初期値0。
    weight_sum = 0
    value_sum = 0
    # 評価値の高いものからループを回す
    for index, target in target_df.iterrows():
        # 制約条件をクリアしたら採択
        if weight_sum + target['weight'] <= W:
            weight_sum += target['weight']
            target['result'] = 1
            value_sum += target['value']

    print(target_df)
    print("---answer---")
    print('Ans, ' + str(value_sum))


if __name__ == '__main__':

    #(1+ε)近似アルゴリズムの実装
    start = time.time()
    approx()
    elapsed_time = time.time() -start
    print('elapsed_time:{0}'.format(elapsed_time) + '[sec]')
