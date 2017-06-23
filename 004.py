string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
firsts = [1, 5, 6, 7, 8, 9, 15, 16, 19]

words = string.split()

elements = []
for i, word in enumerate(words):
    e = word[:1] if i + 1 in firsts else word[:2]
    elements.append(e)

print(elements)

