# 形態素を表すクラスMorphを実装せよ．
# このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）
# をメンバ変数に持つこととする．
# さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，
# 各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ． 

nlp30 = __import__('030')

class Morph:
    def __init__(self, obj):
        self.surface = obj['surface']
        self.base    = obj['base']
        self.pos     = obj['pos']
        self.pos1    = obj['pos1']

    def string(self):
        attrs = [self.surface, self.base, self.pos, self.pos1]
        return ','.join(attrs)


def run():
    words  = nlp30.sentences(path='./data/neko.txt.cabocha')[2]
    words  = [w for w in words if w[0] != '*']
    words  = [nlp30.parse_word(w) for w in words if w[0] != '*']
    morphs = [Morph(w) for w in words]
    strs   = [m.string() for m in morphs]
    print(strs)

if __name__ == '__main__':
    run()

