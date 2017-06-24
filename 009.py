import random

def shuffle(string):
    words = string.split(' ')

    shuffled = []
    for word in words:
        if len(word) > 4:
            chars = [c for c in word[1:-1]]
            random.shuffle(chars)
            word = word[0] + ''.join(chars) + word[-1]
        shuffled.append(word)

    return ' '.join(shuffled)


row = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

print(shuffle(row))

