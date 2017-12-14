# 38. ヒストグラム
# 単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．

import numpy as np
import matplotlib.pyplot as plt

nlp36 = __import__('036')

def run():
    counts = [w[1] for w in nlp36.word_counts()]
    x = np.array(counts)
    plt.hist(x, bins = 100)
    plt.show()

if __name__ == '__main__':
    print(run())
