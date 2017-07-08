# 36. 単語の出現頻度
# 文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．

nlp33 = __import__('033')

def run():
    words = nlp33.words()

    count = {}
    for word in words:
        key = (word['base'], word['pos'], word['pos1'])
        if key not in count:
            count[key] = 0

        count[key] += 1

    count = sorted(count.items(), key = lambda x:x[1], reverse=True)
    bases = [c[0][0] for c in count]
    return bases


if __name__ == '__main__':
    print(run())
