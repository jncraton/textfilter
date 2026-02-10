# textfilter

[filter.lua](filter.lua) reduces token counts in text documents by removing non-essential formatting and elements. It is used by pandoc to strip attributes, images, citations, and other metadata.

## Usage

```sh
pandoc input.epub --lua-filter=filter.lua -o output.md
```

## Benchmarks

Fetch sample documents and run benchmarks with the following command.

```
make bench
```

Benchmarks generate filtered and unfiltered markdown versions of the input files for comparison.

### Tokenization

Token counts are calculated using the gemma-3-270m tokenizer. This tool helps with the stewardship of computational resources by minimizing unnecessary data.
