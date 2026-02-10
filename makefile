all: faulkner.epub

faulkner.epub:
	curl -fSL 'https://standardebooks.org/ebooks/william-faulkner/as-i-lay-dying/downloads/william-faulkner_as-i-lay-dying.epub?source=download' -o faulkner.epub

clean:
	rm -f faulkner.epub
