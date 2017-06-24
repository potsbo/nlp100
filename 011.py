f = open('./data/hightemp.txt', 'r')

for line in f:
    print(line.replace('\t', ' '), end='')

print(nlines)
