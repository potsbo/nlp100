def n_gram(elements, n=2):
    size = len(elements)
    return {tuple(elements[i:min(size, i + 2)]) for i, e in enumerate(elements)}

def char_bi_gram(string):
    return n_gram([c for c in string], 2)

first = "paraparaparadise"
second = "paragraph"

firsts = char_bi_gram(first)
seconds = char_bi_gram(second)

print(firsts & seconds)
print(firsts | seconds)
print(firsts - seconds)
print(seconds - firsts)
print({('s','e')} in (firsts & seconds))
