# 31. 動詞
# 動詞の表層形をすべて抽出せよ．

nlp30 = __import__('030')

def verbs():
    sentences = nlp30.run()
    words = [word for sentence in sentences for word in sentence]
    return [word for word in words if word['pos'] == '動詞']

def run():
    return [verb['surface'] for verb in verbs()]

if __name__ == '__main__':
    print(run())
