import sys
import subprocess
from tokenizers import Tokenizer


def load_tokenizer():
    return Tokenizer.from_pretrained(
        "jncraton/gemma-3-270m-ct2-int8",
        revision="4cbd19d0c1e4c4375ac9bd9c5d6c586ada6a60c9",
    )


def count_tokens(text, tokenizer):
    return len(tokenizer.encode(text).ids)


def run_pandoc(input_file, use_filter=False, wrap="auto"):
    cmd = ["pandoc", "-t", "markdown", "--wrap", wrap, input_file]
    if use_filter:
        cmd.extend(["--lua-filter", "filter.lua"])

    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return result.stdout


def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    filenames = sys.argv[1:]
    tokenizer = load_tokenizer()

    total_generic = 0
    total_nowrap = 0
    total_filtered_wrap = 0
    total_filtered_nowrap = 0

    with open("bench.tsv", "w", encoding="utf-8") as f:
        f.write("file\tgeneric\tnowrap\tfiltered_wrap\tfiltered_nowrap\timprovement\n")

        for filename in filenames:
            generic_text = run_pandoc(filename, use_filter=False)
            nowrap_text = run_pandoc(filename, use_filter=False, wrap="none")
            filtered_wrap_text = run_pandoc(filename, use_filter=True, wrap="auto")
            filtered_nowrap_text = run_pandoc(filename, use_filter=True, wrap="none")

            with open(f"{filename}-unfiltered.md", "w", encoding="utf-8") as f_out:
                f_out.write(generic_text)

            with open(f"{filename}-filtered.md", "w", encoding="utf-8") as f_out:
                f_out.write(filtered_nowrap_text)

            generic_tokens = count_tokens(generic_text, tokenizer)
            nowrap_tokens = count_tokens(nowrap_text, tokenizer)
            filtered_wrap_tokens = count_tokens(filtered_wrap_text, tokenizer)
            filtered_nowrap_tokens = count_tokens(filtered_nowrap_text, tokenizer)

            total_generic += generic_tokens
            total_nowrap += nowrap_tokens
            total_filtered_wrap += filtered_wrap_tokens
            total_filtered_nowrap += filtered_nowrap_tokens

            improvement = (
                (generic_tokens - filtered_nowrap_tokens) / generic_tokens * 100
            )

            row = f"{filename}\t{generic_tokens}\t{nowrap_tokens}\t{filtered_wrap_tokens}\t{filtered_nowrap_tokens}\t{improvement:.2f}%\n"
            f.write(row)
            sys.stdout.write(row)

        if total_generic > 0:
            total_improvement = (
                (total_generic - total_filtered_nowrap) / total_generic * 100
            )
            agg_row = f"Total\t{total_generic}\t{total_nowrap}\t{total_filtered_wrap}\t{total_filtered_nowrap}\t{total_improvement:.2f}%\n"
            f.write(agg_row)
            sys.stdout.write(agg_row)


if __name__ == "__main__":
    main()
