f = open('./data/hightemp.txt', 'r')

nlines = 0
for line in f:
    nlines += 1

print(nlines)
