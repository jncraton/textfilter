SOURCES = faulkner.epub constitution.html gruber.html

all: $(SOURCES)

faulkner.epub:
	curl -fSL 'https://standardebooks.org/ebooks/william-faulkner/as-i-lay-dying/downloads/william-faulkner_as-i-lay-dying.epub?source=download' -o faulkner.epub

constitution.html:
	curl -fSL 'https://constitutioncenter.org/the-constitution/full-text' -o $@

gruber.html:
	curl -fSL 'https://daringfireball.net/projects/markdown/' -o $@

bench: $(SOURCES)
	uv run python3 bench.py $(SOURCES)

clean:
	rm -f $(SOURCES)
	rm -f *-generic.md *-nowrap.md *-filtered_wrap.md *-filtered_nowrap.md
	rm -rf .venv venv uv.lock
