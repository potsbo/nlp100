# 25. テンプレートの抽出
# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．

import json
import re


def get_template_section(filename):
    f = open(filename)
    lines = json.load(f)['text'].split('\n')
    end_template = re.compile(r'^}}$')
    start_template = re.compile(r'^{{基礎情報(.+)$')

    template_started = False

    fields = []
    for line in lines:
        if not template_started:
            if start_template.search(line):
                template_started = True
            continue

        if end_template.search(line):
            break

        fields.append(line)

    return ''.join(['\n' + l for l in fields]).split('\n|')

def fields_to_dict(fields):
    field_match = re.compile(r'^(.+) = (.+)$')
    dic = {}
    for line in fields:
        result = field_match.search(line)
        if result:
            key = result.group(1)
            value = result.group(2)
            dic[key] = value

    return dic


def run():
    filename = './data/020.txt'
    fields = get_template_section(filename)
    dic = fields_to_dict(fields)
    print(dic)


if __name__ == '__main__':
    run()
