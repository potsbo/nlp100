# 43. 名詞を含む文節が動詞を含む文節に係るものを抽出
# 名詞を含む文節が，動詞を含む文節に係るとき，
# これらをタブ区切り形式で抽出せよ．
# ただし，句読点などの記号は出力しないようにせよ．

nlp41 = __import__('041')

def run():
    sentences = nlp41.chunks()

    surfaces = []
    for chunks in sentences:
        for chunk in chunks:
            if not chunk.include_noun():
                continue

            if not chunk.dst > 0:
                continue
            
            dst = chunks[chunk.dst]
            if not dst.include_verb():
                continue

            surface = chunk.surface(exclude_symbols=True)
            surface += "\t"
            surface += dst.surface(exclude_symbols=True)
            surfaces.append(surface)

    return surfaces


if __name__ == '__main__':
    surfaces = run()
    for surface in surfaces:
        print(surface)
