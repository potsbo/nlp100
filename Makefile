data/col1.txt: data/hightemp.txt
	python 012.py

data/col2.txt: data/hightemp.txt
	python 012.py

data/jawiki-country.json.gz:
	curl http://www.cl.ecei.tohoku.ac.jp/nlp100/data/jawiki-country.json.gz > ./data/jawiki-country.json.gz

data/jawiki-country.json: data/jawiki-country.json.gz
	gzip -d ./data/jawiki-country.json.gz

data/hightemp.txt:
	curl http://www.cl.ecei.tohoku.ac.jp/nlp100/data/hightemp.txt > ./data/hightemp.txt

data/neko.txt:
	curl http://www.cl.ecei.tohoku.ac.jp/nlp100/data/neko.txt > ./data/neko.txt

data/neko.txt.mecab: data/neko.txt
	mecab ./data/neko.txt > ./data/neko.txt.mecab
