# 39. Zipfの法則
# 単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．

import numpy as np
import matplotlib.pyplot as plt
import math

nlp36 = __import__('036')

def run():
    counts = [w[1] for w in nlp36.word_counts()]
    x = np.array(counts)
    high = math.ceil(math.log10(max(x)))
    low  = math.floor(math.log10(min(x)))
    bins=np.logspace(low, high, 20)
    plt.hist(x, bins=bins, log=True)
    plt.xscale("log")
    plt.show()

if __name__ == '__main__':
    print(run())
