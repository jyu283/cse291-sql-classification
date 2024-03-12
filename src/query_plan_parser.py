import sys
import csv
import json
import pprint


class QueryPlanParser:
    def __init__(self, csv_file: str, query_ids_file: str):
        self.query_plans = dict()

        query_ids = self.get_query_ids_from_file(query_ids_file)

        with open(csv_file, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            i = 0
            for row in reader:
                query_id = query_ids[i]
                raw_json = row.get("content")
                query_plan = json.loads(raw_json)
                self.query_plans[query_id] = query_plan
                i += 1
            pprint.pprint(self.query_plans)

    def get_query_ids_from_file(self, query_ids_file: str):
        with open(query_ids_file, "r") as fp:
            lines = fp.readlines()
            for i in range(len(lines)):
                lines[i] = lines[i].strip()
            return lines


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python query_plan_parser.py queryplan.json query_ids_file")
        exit(1)

    parser = QueryPlanParser(sys.argv[1], sys.argv[2])
