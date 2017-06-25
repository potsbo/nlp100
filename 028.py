# 28. MediaWikiマークアップの除去
# 27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．

import re

nlp27 = __import__('027')


def remove_lang(dic):
    for (k,v) in dic.items():
        dic[k] = re.sub(r"\{\{(.+)\|(.+)\|(.+)\}\}", r'\3', v)
    return dic


def remove_br(dic):
    for (k,v) in dic.items():
        dic[k] = re.sub(r"<br ?/>", '', v)
    return dic

def remove_ref(dic):
    for (k,v) in dic.items():
        dic[k] = re.sub(r"<ref(.*?)>(.+)</ref>", '', v)
        dic[k] = re.sub(r"<ref(.*?)/>", '', dic[k])
    return dic


def run():
    dic = nlp27.run()
    dic = remove_lang(dic)
    dic = remove_br(dic)
    dic = remove_ref(dic)
    return dic


if __name__ == '__main__':
    print(run())
