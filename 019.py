# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．

lines = [line.split('\t') for line in open('./data/hightemp.txt')]

count = {}
for line in lines:
    prov = line[0]
    if prov not in count:
        count[prov] = 0

    count[prov] += 1

count = sorted(count.items(), key=lambda item:item[1], reverse=True)

output = []
for (prov,_) in count:
    cities = [line for line in lines if line[0] == prov]
    output.append(cities)

output = [item for sublist in output for item in sublist]
output = ''.join(['\t'.join(item) for item in output])

print(output)
