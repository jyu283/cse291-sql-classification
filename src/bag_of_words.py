"""
Produce bag-of-words from query CSV files (see data/*.csv).
"""

import csv
import sys

from collections import namedtuple

from typing import TextIO, List, Set, Tuple

QueryRecord = namedtuple("QueryRecord", ["id", "text", "time"])


class BagOfWords:
    def __init__(self, csv_file: TextIO):
        self.csv_file = csv_file

        with open(self.csv_file, "r") as fp:
            reader = csv.DictReader(fp)
            self.rows: List[Tuple[str, str, float]] = []
            for row in reader:
                record = QueryRecord(
                    id=row.get("TPCDS_Query_ID"),
                    text=row.get("QUERY_TEXT"),
                    time=float(row.get("TOTAL_ELAPSED_TIME")),
                )
                self.rows.append(record)

        print(f"{len(self.rows)} queries processed.")

        self.bag: Set[str] = set()

    def tokenize_query(self, query_text: str) -> List[str]:
        """sanitize a query for tokenization."""
        return (
            query_text.lower()
            .replace("'", "")
            .replace(",", "")
            .replace('"', "")
            .replace(";", "")
            .replace("(", " ")
            .replace(")", " ")
            .replace(".", " ")
            .replace("/", " ")
            .replace(">", " ")
            .replace("<", " ")
            .replace("=", " ")
            .replace("+", " ")
            .replace("-", " ")
            .replace("*", " ")
            .split()
        )

    def process(self):
        total_tokens = 0
        for _, text, _ in self.rows:
            tokens = self.tokenize_query(text)
            total_tokens += len(tokens)
            self.bag.update(self.tokenize_query(text))
        
        print("Bag of words: ")
        print(self.bag)
        print(f"{len(self.bag)} unique tokens from {total_tokens} total.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("python bag_of_words.py csv_file")
        sys.exit(1)

    bow = BagOfWords(sys.argv[1])
    bow.process()
