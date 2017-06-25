# 29. 国旗画像のURLを取得する
# テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）

import json
import urllib.parse, urllib.request

nlp28 = __import__('028')

def filename_to_url(filename):
    query = {
        'action': 'query',
        'titles': 'File:' + urllib.parse.quote(filename),
        'format': 'json',
        'prop':   'imageinfo',
        'iiprop': 'url',
    }

    query_str = '&'.join(['='.join([k,v]) for (k,v) in query.items()])

    url = 'https://www.mediawiki.org/w/api.php?' + query_str

    request = urllib.request.Request(url)
    connection = urllib.request.urlopen(request)

    data = json.loads(connection.read().decode())

    url = data['query']['pages']['-1']['imageinfo'][0]['url']
    return url


def run():
    dic = nlp28.run()
    filename = dic['国旗画像']

    return filename_to_url(filename)


if __name__ == '__main__':
    print(run())
