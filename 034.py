# 34. 「AのB」
# 2つの名詞が「の」で連結されている名詞句を抽出せよ．

nlp30 = __import__('030')

def find_no(sentence):
    words = [w for w in sentence]
    phrases = []
    for i, _ in enumerate(words):
        if i + 2 > len(words) - 1:
            break

        if words[i]['pos'] == '名詞' and words[i+1]['surface'] == 'の' and words[i+2]['pos'] == '名詞':
            phrase = ''.join([word['surface'] for word in words[i:i+3]])
            phrases.append(phrase)

    return phrases

def run():
    noes = []
    for sentence in nlp30.sentences():
        phrases = find_no(sentence)
        noes.append(phrases)

    return [p for ps in noes for p in ps]

if __name__ == '__main__':
    print(run())
