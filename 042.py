# 42. 係り元と係り先の文節の表示
# 係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．
# ただし，句読点などの記号は出力しないようにせよ．

nlp41 = __import__('041')

def run():
    sentences = nlp41.chunks()

    surfaces = []
    for chunks in sentences:
        for chunk in chunks:
            surface = chunk.surface(exclude_symbols=True)
            if chunk.dst > 0:
                surface += "\t" + chunks[chunk.dst].surface(exclude_symbols=True)
            surfaces.append(surface)

    return surfaces


if __name__ == '__main__':
    surfaces = run()
    for surface in surfaces:
        print(surface)
