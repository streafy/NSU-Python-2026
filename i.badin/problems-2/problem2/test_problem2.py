import unittest
from pathlib import Path

from problem2 import (
    build_latin_english_dictionary,
    convert_dictionary,
    convert_dictionary_file,
)


class TestLatinEnglishDictionary(unittest.TestCase):
    def test_example_from_task(self):
        english_latin_lines = [
            "apple - malum, pomum, popula",
            "fruit - baca, bacca, popum",
            "punishment - malum, multa",
        ]

        self.assertEqual(
            convert_dictionary(english_latin_lines),
            [
                "baca - fruit",
                "bacca - fruit",
                "malum - apple, punishment",
                "multa - punishment",
                "pomum - apple",
                "popula - apple",
                "popum - fruit",
            ],
        )

    def test_dictionary_is_inversed(self):
        english_latin_lines = [
            "apple - malum, pomum",
            "punishment - malum",
        ]

        self.assertEqual(
            build_latin_english_dictionary(english_latin_lines),
            {
                "malum": {"apple", "punishment"},
                "pomum": {"apple"},
            },
        )

    def test_words_are_sorted_alphabetically(self):
        english_latin_lines = [
            "zebra - delta, alpha",
            "apple - delta",
            "monkey - beta",
        ]

        self.assertEqual(
            convert_dictionary(english_latin_lines),
            [
                "alpha - zebra",
                "beta - monkey",
                "delta - apple, zebra",
            ],
        )

    def test_duplicate_translations_are_removed(self):
        english_latin_lines = [
            "apple - malum, malum",
            "punishment - malum",
        ]

        self.assertEqual(
            convert_dictionary(english_latin_lines),
            ["malum - apple, punishment"],
        )

    def test_empty_input(self):
        self.assertEqual(convert_dictionary([]), [])

    def test_convert_dictionary_file(self):
        problem_dir = Path(__file__).resolve().parent
        source_path = problem_dir / "english_latin.txt"
        result_path = problem_dir / "latin_english.txt"

        convert_dictionary_file(str(source_path), str(result_path))

        self.assertEqual(
            result_path.read_text(encoding="utf-8"),
            "baca - fruit\n"
            "bacca - fruit\n"
            "malum - apple, punishment\n"
            "multa - punishment\n"
            "pomum - apple\n"
            "popula - apple\n"
            "popum - fruit\n",
        )


if __name__ == "__main__":
    unittest.main()
