"""
Produce bag-of-words from query CSV files (see data/*.csv).
"""

import csv
import sys
import pandas as pd
from collections import namedtuple, OrderedDict
from typing import TextIO, List, Set, Tuple

QueryRecord = namedtuple("QueryRecord", ["id", "text", "time"])


class BagOfWords:
    """
    Process a query result CSV file (currently only in Snowflake export format)
    into a bag-of-words.
    """

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

    def compute_bag(self) -> Set[str]:
        bag: Set[str] = set()
        total_tokens = 0
        for _, text, _ in self.rows:
            tokens = self.tokenize_query(text)
            total_tokens += len(tokens)
            bag.update(self.tokenize_query(text))

        print(f"{len(bag)} unique tokens from {total_tokens} total.")

        return bag

    def vectorize_query(self, query: str) -> OrderedDict[str, int]:
        tokens = self.tokenize_query(query)
        vector: OrderedDict[str, int] = OrderedDict()
        for token in sorted(self.bag):
            vector[token] = 0
        for token in tokens:
            vector[token] += 1
        return vector

    def process(self) -> List[pd.DataFrame]:
        """
        Process CSV file into a list of pandas DataFrame objects.
        Each DataFrame contains:
        {
            "query_id": [query id],
            "query_text": [original SQL query statement],
            "elapsed_time": [measured query execution time],
            "bow_vector": {
                "word1": [occurrence],
                "word2": [occurrence],
                "word3": [occurrence],
                ...
            }
        }
        """
        self.bag = self.compute_bag()
        data: List[pd.DataFrame] = []
        for query_id, query_text, elapsed_time in self.rows:
            vector = self.vectorize_query(query_text)
            df = pd.DataFrame(
                {
                    "query_id": query_id,
                    "query_text": query_text,
                    "elapsed_time": elapsed_time,
                    "bow_vector": vector,
                }
            )
            data.append(df)
        return data


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("python bag_of_words.py csv_file")
        sys.exit(1)

    bow = BagOfWords(sys.argv[1])
    data = bow.process()
