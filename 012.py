f = open('./data/hightemp.txt', 'r')

columns = []
for line in f:
    cols = line.split('\t')
    columns.append(cols[0:2])

col1 = '\n'.join([line[0] for line in columns])
col2 = '\n'.join([line[1] for line in columns])

open('./result/col1.txt', 'w').write(col1)
open('./result/col2.txt', 'w').write(col2)
