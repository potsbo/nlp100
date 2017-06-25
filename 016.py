# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

import sys, math

if len(sys.argv) < 2:
    print('Input a number.')
    exit()

n = int(sys.argv[1])
if not n:
    print('Input a number.')
    exit()

lines = [line for line in open('./data/hightemp.txt')]
size = len(lines)
step = math.ceil(size / n)
for i in range(0, size, step):
    print(''.join(lines[i:i + step]))

print(output, end='')
