# 17. １列目の文字列の異なり
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

lines = [line for line in open('./data/hightemp.txt')]
provs = [line.split('\t')[0] for line in lines]
provs = list(set(provs))

print(provs)

