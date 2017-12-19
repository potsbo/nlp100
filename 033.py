# 33. サ変名詞
# サ変接続の名詞をすべて抽出せよ．

nlp30 = __import__('030')

def words():
    sentences = nlp30.analyzed_sentences()
    return [word for sentence in sentences for word in sentence]

def run():
    return [w for w in words() if w['pos'] == '名詞' and w['pos1'] == 'サ変接続']

if __name__ == '__main__':
    print(run())
