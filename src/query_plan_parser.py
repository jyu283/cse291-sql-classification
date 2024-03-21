"""
python src/query_plan_parser.py data/query_plans/query_plans.csv
"""

import sys
import csv
import json
import pprint
import pandas as pd
from collections import namedtuple, defaultdict
from typing import List

QueryRecord = namedtuple("QueryRecord", ["id", "text", "time", "plan"])


class QueryPlanParser:
    def __init__(self, csv_file: str):
        self.queries = []
        self.all_features = set()

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
    
    def extract_features(self, query_plan: dict) -> dict:
        total_bytes = query_plan["GlobalStats"]["bytesAssigned"]
        operations_count = defaultdict(int)
        for operations in query_plan["Operations"]:
            for op in operations:
                operations_count[op['operation']] += 1

        features = {
            "total_bytes": total_bytes,
        }
        for op, count in operations_count.items():
            features["num_" + op] = count
        
        for feature in features:
            self.all_features.add(feature)

        return features

    def process(self) -> pd.DataFrame:
        dataset = []
        for query_id, query_text, query_time, query_plan in self.queries:
            data = {
                # "query_id": query_id,
                # "query_text": query_text,
                "elapsed_time": query_time,
                "features": self.extract_features(query_plan)
            }
            dataset.append(data)
        
        for data in dataset:
            features = data["features"]
            for feat in self.all_features:
                if feat not in features:
                    features[feat] = 0
            for feat in sorted(data["features"].keys()):
                data[feat] = data["features"][feat]
            del data["features"]
        
        df = pd.DataFrame(dataset)
        print(df)
        return df

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python query_plan_parser.py queryplan.json")
        exit(1)

    parser = QueryPlanParser(sys.argv[1])
    parser.process()
