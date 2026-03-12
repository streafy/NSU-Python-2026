from collections import defaultdict
from pathlib import Path
import sys


def parse_dictionary_line(line: str) -> tuple[str, list[str]]:
    english_word, _, latin_words_part = line.partition(" - ")
    latin_words = [latin_word.strip() for latin_word in latin_words_part.split(",")]
    return english_word.strip(), latin_words


def build_latin_english_dictionary(english_latin_lines: list[str]) -> dict[str, set[str]]:
    latin_to_english: defaultdict[str, set[str]] = defaultdict(set)

    for line in english_latin_lines:
        if not line.strip():
            continue

        english_word, latin_words = parse_dictionary_line(line.strip())
        for latin_word in latin_words:
            latin_to_english[latin_word].add(english_word)

    return dict(latin_to_english)


def format_dictionary(latin_english_dictionary: dict[str, set[str]]) -> list[str]:
    return [
        f"{latin_word} - {', '.join(sorted(latin_english_dictionary[latin_word]))}"
        for latin_word in sorted(latin_english_dictionary)
    ]


def convert_dictionary(english_latin_lines: list[str]) -> list[str]:
    latin_english_dictionary = build_latin_english_dictionary(english_latin_lines)
    return format_dictionary(latin_english_dictionary)


def convert_dictionary_file(source_path: str, result_path: str) -> None:
    source_file = Path(source_path)
    result_file = Path(result_path)

    result_lines = convert_dictionary(source_file.read_text(encoding="utf-8").splitlines())
    result_text = "\n".join(result_lines)
    if result_text:
        result_text += "\n"

    result_file.write_text(result_text, encoding="utf-8")


def main():
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python problem2.py <source_path> <result_path>")

    convert_dictionary_file(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
