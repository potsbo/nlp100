# 22. カテゴリ名の抽出
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

import json
import re

f = open('./data/020.txt')
lines = json.load(f)['text'].split('\n')

category_match = re.compile(r'^\[\[Category:(.*)\]\]$')

for line in lines:
    result = category_match.search(line)

    if result is None:
        continue

    print(result.group(1).split('|')[0])
