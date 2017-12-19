HOST := http://www.cl.ecei.tohoku.ac.jp/nlp100

data:
	mkdir -p $@

data/col1.txt data/col2.txt: data/hightemp.txt data
	python 012.py

data/jawiki-country.json.gz: data
	curl $(HOST)/$< > $@

data/jawiki-country.json: data/jawiki-country.json.gz data
	gzip -d $<

data/hightemp.txt data/neko.txt: data
	curl $(HOST)/$@ > $@

data/neko.txt.mecab: data/neko.txt data
	mecab $@ > $@

data/020.txt: data/jawiki-country.json data
	python 020.py
