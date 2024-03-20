from pathlib import Path
import pandas as pd
import tabulate
from src.decision_tree import SQLQueryClassifier


def main():
    # Training data folder
    data_dir: Path = Path(__file__).parent.parent / "data"
    datasets = [
        "TPC-DS-10TB-Snowflake.csv",
        "TPC-DS-100TB-Snowflake.csv"
    ]
    dataset_paths = [data_dir / dataset for dataset in datasets]

    # Evaluate on the decision tree classifier
    results = []
    thresholds = [4000, 8000, 12000, 16000, 20000, 30000]  # + [100, 1000, 100000]

    for dataset_path in dataset_paths:
        for threshold in thresholds:
            for test_size in [0.2, 0.4, 0.6, 0.8]:
                try:
                    # Evaluate
                    classifier = SQLQueryClassifier(
                        dataset_path,
                        threshold=threshold,
                        test_size=test_size,
                        valid_size_over_train=0.3,
                        random_state=42,
                    )
                    X, y = classifier.load_and_preprocess()
                    X_train, X_val, X_test, y_train, y_val, y_test = classifier.split_data(X, y)
                    stat = classifier.train_and_evaluate(X_train, y_train, X_test, y_test, verbose=False)

                    # Add some metadata
                    stat['dataset'] = dataset_path.name
                    stat['threshold'] = threshold
                    stat['test_size'] = test_size

                    results.append(stat)
                    # print(f"Evaluated {dataset_path.name} with threshold {threshold}: {stat}")
                except Exception as e:
                    print(f"Failed to evaluate {dataset_path.name} with threshold {threshold}")

    # Save results to a CSV file
    df = pd.DataFrame(results)
    df.to_csv("eval_result_decision_tree_results.csv", index=False)
    print(tabulate.tabulate(df, headers='keys', tablefmt='pretty'))

    return


if __name__ == '__main__':
    main()
