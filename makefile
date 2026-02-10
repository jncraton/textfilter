all: faulkner.epub constitution.html

faulkner.epub:
	curl -fSL 'https://standardebooks.org/ebooks/william-faulkner/as-i-lay-dying/downloads/william-faulkner_as-i-lay-dying.epub?source=download' -o faulkner.epub

constitution.html:
	curl -fSL 'https://constitutioncenter.org/the-constitution/full-text' -o $@

clean:
	rm -f faulkner.epub constitution.html
	rm -rf .venv venv uv.lock
