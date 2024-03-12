#!/bin/python3

import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: snowflake_get_plans.py query_ids_file")
        sys.exit(1)

    with open(sys.argv[1], "r") as fp:
        lines = fp.readlines()
        queries = []
        for line in lines:
            query_id = line.strip()
            queries.append(f"SELECT * FROM TABLE(RESULT_SCAN(\'{query_id}\'))\n")
        query = "UNION\n".join(queries)
        print(query)
