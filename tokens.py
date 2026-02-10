import sys
from tokenizers import Tokenizer


def load_tokenizer():
    return Tokenizer.from_pretrained("jncraton/gemma-3-270m-ct2-int8")


def count_tokens(text, tokenizer):
    return len(tokenizer.encode(text).ids)


def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    filename = sys.argv[1]
    tokenizer = load_tokenizer()

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    print(count_tokens(content, tokenizer))


if __name__ == "__main__":
    main()
