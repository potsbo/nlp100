# 27. 内部リンクの除去
# 26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．

import re

nlp26 = __import__('026')

def run():
    dic = nlp26.run()
    for (k,v) in dic.items():
        dic[k] = re.sub(r"\[\[([^\|\]]+?\|)*(.+?)\]\]", r'\2', v)
    return dic

if __name__ == '__main__':
    print(run())
