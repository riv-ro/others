import numpy as np
from pandas import DataFrame

# 制約条件より
weights = np.array([6, 5, 1, 3])
# 目的関数より
values = np.array([1, 8, 1, 2])
# xの配列。初期値はすべて0とする。採択した時に1にする。
results = np.array([0, 0, 0, 0])
# 評価値を算出。
evaluates = values/weights
# DataFrameにまとめる
target_df = DataFrame(np.c_[evaluates, weights, values, results], index=['x1', 'x2', 'x3', 'x4'], columns = ['evaluate', 'weight', 'value', 'result'])
# evaluateの値で降順に並び替える
target_df = target_df.sort_values(['evaluate'])

# 採択した項目のweightの和。初期値0。
weight_sum = 0

# 評価値の高いものからループを回す
for index, target in target_df.iterrows():
    # 制約条件をクリアしたら採択
    if weight_sum + target['weight'] <= 6:
        weight_sum += target['weight']
        target['result'] = 1

print(target_df)
print("---answer---")
print(target_df['result'])
