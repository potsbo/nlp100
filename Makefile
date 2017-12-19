data/neko.txt:
	curl http://www.cl.ecei.tohoku.ac.jp/nlp100/data/neko.txt > ./data/neko.txt

data/neko.txt.mecab: data/neko.txt
	mecab ./data/neko.txt > ./data/neko.txt.mecab
