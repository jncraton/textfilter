import sys
import subprocess
from tokenizers import Tokenizer


def load_tokenizer():
    return Tokenizer.from_pretrained("jncraton/gemma-3-270m-ct2-int8")


def count_tokens(text, tokenizer):
    return len(tokenizer.encode(text).ids)


def run_pandoc(input_file, use_filter=False):
    cmd = ["pandoc", "-t", "markdown", input_file]
    if use_filter:
        cmd.extend(["--lua-filter", "filter.lua"])

    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return result.stdout


def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    filename = sys.argv[1]
    tokenizer = load_tokenizer()

    generic_text = run_pandoc(filename, use_filter=False)
    filtered_text = run_pandoc(filename, use_filter=True)

    generic_tokens = count_tokens(generic_text, tokenizer)
    filtered_tokens = count_tokens(filtered_text, tokenizer)

    improvement = (generic_tokens - filtered_tokens) / generic_tokens * 100

    print(f"Generic: {generic_tokens}")
    print(f"Filtered: {filtered_tokens}")
    print(f"Improvement: {improvement:.2f}%")


if __name__ == "__main__":
    main()
