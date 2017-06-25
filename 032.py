# 32. 動詞の原形
# 動詞の原形をすべて抽出せよ．

nlp31 = __import__('031')

def run():
    return [verb['base'] for verb in nlp31.verbs()]

if __name__ == '__main__':
    print(run())
