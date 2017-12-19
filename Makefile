HOST := http://www.cl.ecei.tohoku.ac.jp/nlp100

# Raw data
data/hightemp.txt data/neko.txt:
	mkdir -p data && curl $(HOST)/$@ > $@

# Chapter 2
data/col1.txt data/col2.txt: data/hightemp.txt
	python 012.py

# Chapter 3
data/jawiki-country.json.gz:
	make -p data && curl $(HOST)/$@ > $@

data/jawiki-country.json: data/jawiki-country.json.gz
	gzip -d < $< > $@

data/020.txt: data/jawiki-country.json
	python 020.py

# Chapter 4
data/neko.txt.mecab: data/neko.txt
	mecab $< > $@

# Chapter 5
data/neko.txt.cabocha: data/neko.txt
	cabocha $< > $@
