import time
import numpy as np

def DP():
    # N = int(input('n: '))
    # W = int(input('W: '))
    # w = list(map(int, input('w: ').split()))
    # v = list(map(int, input('v: ').split()))

    # w = [2,2,1,3,4,2,5,7,7,5,3,3,1,7,5,9,4,9]
    # v = [4,5,2,8,3,5,6,7,3,6,2,6,7,6,1,9,6,5]
    # N = len(w)
    # W = 30

    w = np.load('./weight_100.npy')
    v = np.load('./value_100.npy')
    N = len(w)
    W = 30

    print('input------')
    print(N)
    print(W)
    print(w)
    print(v)
    print('-----------')

    dp = [[0 for i in range(W + 1)] for j in range(N + 1)]

    for j in range(N) :
        for i in range(N - 1, -1, -1) :
            for j in range(W + 1) :
                if j < w[i] :
                    dp[i][j] = dp[i+1][j]
                else :
                    dp[i][j] = max(dp[i+1][j], dp[i+1][j-w[i]]+v[i])
    print('Ans, ' + str(dp[0][W]))

if __name__ == '__main__':

    #漸化式を用いた実装
    start = time.time()
    DP()
    elapsed_time = time.time() - start
    print ('elapsed_time:{0}'.format(elapsed_time) + '[sec]')
