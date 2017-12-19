HOST := http://www.cl.ecei.tohoku.ac.jp/nlp100

data:
	mkdir -p $@

# Raw data
data/hightemp.txt data/neko.txt: data
	curl $(HOST)/$@ > $@

# Chapter 2
data/col1.txt data/col2.txt: data/hightemp.txt data
	python 012.py

# Chapter 3
data/jawiki-country.json.gz: data
	curl $(HOST)/$@ > $@

data/jawiki-country.json: data/jawiki-country.json.gz data
	gzip -d < $< > $@

data/020.txt: data/jawiki-country.json data
	python 020.py

# Chapter 4
data/neko.txt.mecab: data/neko.txt data
	mecab $< > $@

# Chapter 5
data/neko.txt.cabocha: data/neko.txt data
	cabocha $< > $@

