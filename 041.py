# 40に加えて，文節を表すクラスChunkを実装せよ．
# このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），
# 係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．
# さらに，入力テキストのCaboChaの解析結果を読み込み，
# １文をChunkオブジェクトのリストとして表現し，
# 8文目の文節の文字列と係り先を表示せよ．第5章の残りの問題では，
# ここで作ったプログラムを活用せよ．

nlp30 = __import__('030')
nlp40 = __import__('040')

class Chunk:
    def __init__(self, words):
        morphs       = [nlp30.parse_word(w) for w in words[1:]]
        self.morphs  = [nlp40.Morph(m) for m in morphs]

        # index
        info        = words[0].split(' ')
        self.idx    = int(info[1])
        self.dst    = int(info[2][:-1])
        self.srcs   = []

    def take_src(self, index):
        self.srcs.append(index)

    def surface(self):
        return ''.join([m.surface for m in self.morphs])

    def string(self):
        return ' '.join([self.surface(), str(self.dst)])


def devide_into_chunks(words):
    chunks = []
    chunk  = []
    for word in words:
        if word[0] == '*':
            if len(chunk) > 0:
                chunks.append(chunk)
                chunk = []
        chunk.append(word)
    chunks.append(chunk)
    return chunks


def run():
    sentence = nlp30.sentences(path='./data/neko.txt.cabocha')[7]
    chunks = devide_into_chunks(sentence)
    chunks = [Chunk(chunk) for chunk in chunks]
    for chunk in chunks:
        src = chunk.idx
        dst = chunk.dst
        chunks[dst].take_src(src)
    return "\n".join([c.string() for c in chunks])

if __name__ == '__main__':
    print(run())
