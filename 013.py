col1 = [e.strip() for e in open('./data/col1.txt')] 
col2 = [e.strip() for e in open('./data/col2.txt')] 

zipped = list(map(list, zip(col1, col2)))
zipped = '\n'.join(['\t'.join(line) for line in zipped])
print(zipped)
