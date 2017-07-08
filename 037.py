# 37. 頻度上位10語
# 出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

nlp36 = __import__('036')
import numpy as np
import matplotlib.pyplot as plt

def run():
    count = nlp36.word_counts()
    bases = [(c[0][0], c[1]) for c in count[:10]]

    height = np.array([b[1] for b in bases])
    label = np.array([b[0] for b in bases])
    plt.bar(range(0,10), height, tick_label=label)
    plt.show()
    return bases

if __name__ == '__main__':
    print(run())
