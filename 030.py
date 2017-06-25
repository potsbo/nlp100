# 30. 形態素解析結果の読み込み
# 形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．

import re

def divide_into_sentences(lines):
    sentences = []
    sentence = []
    for line in lines:
        if line == 'EOS':
            if len(sentence) > 0:
                sentences.append(sentence)
                sentence = []
            continue

        sentence.append(line)

    return sentences

def parse_word(word):
    elements = word.split('\t')
    surface = elements[0]
    elements = elements[1].split(',')
    base = elements[6]
    pos = elements[0]
    pos1 = elements[2]
    return { 'surface': surface, 'base': base, 'pos': pos, 'pos1': pos1 }

def sentences():
    lines = [re.sub('\n', '', line) for line in open('./data/neko.txt.mecab')]

    sentences = divide_into_sentences(lines)

    return [[parse_word(word) for word in sentence] for sentence in sentences]

def run():
    return sentences()

if __name__ == '__main__':
    print(run())
