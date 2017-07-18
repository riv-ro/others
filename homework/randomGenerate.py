import numpy as np

num = 750

#再現性のためにシードを固定
np.random.seed(seed=32)

#重さwと価値vを乱数生成
weight = np.random.randint(1, 10, num)
value = np.random.randint(1, 20, num)
print(weight)
print(value)

#生成した乱数の保存
np.save('weight_'+str(num)+'.npy', weight)
np.save('value_'+str(num)+'.npy', value)
