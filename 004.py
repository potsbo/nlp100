string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
firsts = [1, 5, 6, 7, 8, 9, 15, 16, 19]

words = string.split()

elements = {}
for i, word in enumerate(words):
    num = i + 1
    e = word[:1] if num in firsts else word[:2]
    elements[e] = num

print(elements)

