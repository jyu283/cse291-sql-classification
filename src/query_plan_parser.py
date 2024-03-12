import sys
import csv
import json
import pprint
from collections import namedtuple

QueryRecord = namedtuple("QueryRecord", ["id", "text", "time", "plan"])


class QueryPlanParser:
    def __init__(self, csv_file: str):
        self.queries = []

        with open(csv_file, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                query_id = row.get("QUERY_ID")
                query_plan = json.loads(row.get("content"))
                query_text = row.get("QUERY_TEXT").replace("explain using json ", "")
                query_time = row.get("TOTAL_ELAPSED_TIME")
                self.queries.append(
                    QueryRecord(
                        id=query_id,
                        text=query_text,
                        time=query_time,
                        plan=query_plan,
                    )
                )
            pprint.pprint(self.queries)

    def vectorize_query(self, query: str, query_plan: dict):
        pass


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python query_plan_parser.py queryplan.json")
        exit(1)

    parser = QueryPlanParser(sys.argv[1])
