# 24. ファイル参照の抽出
# 記事から参照されているメディアファイルをすべて抜き出せ．

import json
import re

f = open('./data/020.txt')
lines = json.load(f)['text'].split('\n')

media_match = re.compile(r'^\[\[File:(.+)\]\]$')

for line in lines:
    result = media_match.search(line)

    if result is None:
        continue

    print(result.group(1).split('|')[0])
