HOST := http://www.cl.ecei.tohoku.ac.jp/nlp100

data/col1.txt data/col2.txt: data/hightemp.txt
	python 012.py

data/jawiki-country.json.gz:
	curl $(HOST)/$< > $@

data/jawiki-country.json: data/jawiki-country.json.gz
	gzip -d $<

data/hightemp.txt data/neko.txt:
	curl $(HOST)/$@ > $@

data/neko.txt.mecab: data/neko.txt
	mecab $@ > $@

data/020.txt: data/jawiki-country.json
	python 020.py
