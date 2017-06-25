# 22. カテゴリ名の抽出
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

import json
import re

f = open('./data/020.txt')
lines = json.load(f)['text'].split('\n')

category_match = re.compile(r'^(=+)(.+?)(=+)$')

for line in lines:
    result = category_match.search(line)

    if result is None:
        continue

    title = result.group(2).strip()
    level = len(result.group(1).strip())
    print(level, title)
