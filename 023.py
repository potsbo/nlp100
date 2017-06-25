# 23. セクション構造
# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．

import json
import re

f = open('./data/020.txt')
lines = json.load(f)['text'].split('\n')

category_match = re.compile(r'^\[\[Category:(.*)\]\]$')

for line in lines:
    print(line)
    # result = category_match.search(line)

    # if result is None:
    #     continue

    # print(result.group(1).split('|')[0])
