# 20. JSONデータの読み込み
# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．

import json

f = open('./data/jawiki-country.json', 'r')
pages = [json.loads(line) for line in f]


extracted = None
for page in pages:
    if page['title'] == 'イギリス':
        extracted = page
        break

if extracted is None:
    'イギリス not found.'
    exit()

with open('./data/020.txt', 'w') as outfile:
    outfile.write(json.dumps(extracted, ensure_ascii=False))
