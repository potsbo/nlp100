# 35. 名詞の連接
# 名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．

nlp30 = __import__('030')

def find_chains(sentence):
    words = sentence
    chains = []
    last_index = len(words) - 1

    in_chains = False
    chain_start_point = -1

    for i,_ in enumerate(words):
        if words[i]['pos'] == '名詞':
            if not in_chains:
                chain_start_point = i
            in_chains = True
        else:
            if in_chains and i - chain_start_point > 1:
                chain = ''.join([w['surface'] for w in words[chain_start_point:i]])
                chains.append(chain)
            in_chains = False

    return chains


def run():
    chains = []
    for sentence in nlp30.sentences():
        chains.append(find_chains(sentence))
    return [p for ps in chains for p in ps]

if __name__ == '__main__':
    print(run())
