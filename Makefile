out/index.html: $(wildcard in/*.md)
	python3 autosite.py --auto

.PHONY: clean publish
clean:
	rm -rf out
publish: out/index.html
	rm -rf ~/public_html/p8wiki
	cp -r out ~/public_html/p8wiki
