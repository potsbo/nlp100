def n_gram(elements, n=2):
    size = len(elements)
    return [elements[i:min(size, i + 2)] for i, e in enumerate(elements)]


string = "I am an NLPer"
words = string.split()
chars = [c for c in string]

print(n_gram(chars))
print(n_gram(words))
