# 26. 強調マークアップの除去
# 25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．

import re

nlp25 = __import__('025')

def run():
    dic = nlp25.run()
    for (k,v) in dic.items():
        dic[k] = re.sub(r"'''(.+?)'''", r'\1', v)
    return dic

if __name__ == '__main__':
    print(run())
