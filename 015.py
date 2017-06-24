# 14. 先頭からN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

import sys

if len(sys.argv) < 2:
    print('Input a number.')
    exit()

n = int(sys.argv[1])
if not n:
    print('Input a number.')
    exit()

lines = [line for line in open('./data/hightemp.txt')][-n:]
output = ''.join(lines)

print(output, end='')
