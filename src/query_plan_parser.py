import sys

class QueryPlanParser:
    def __init__(self, json_file: str):
        pass


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Usage: python query_plan_parser.py queryplan.json")
        exit(1)

    parser = QueryPlanParser(sys.argv[1])