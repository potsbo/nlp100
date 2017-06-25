# 21. カテゴリ名を含む行を抽出
# 記事中でカテゴリ名を宣言している行を抽出せよ．

import json
import re

f = open('./data/020.txt')
lines = json.load(f)['text'].split('\n')

category_match = re.compile(r'^\[\[Category:.*\]\]$')

for line in lines:
    if category_match.search(line):
        print(line)
