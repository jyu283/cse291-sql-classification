import argparse

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split, cross_val_score
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
from query_plan_parser import QueryPlanParser
import time


class SQLQueryPlanClassifier:
    def __init__(
        self, csv_path, threshold=14000,
        test_size=0.4,
        valid_size_over_train=0.5,
        random_state=42,
        features: list = None,
    ):
        self.csv_path = csv_path
        self.threshold = threshold
        self.test_size = test_size
        self.valid_size_over_train = valid_size_over_train
        self.random_state = random_state
        self.features = features

    def load_and_preprocess(self):
        parser = QueryPlanParser(self.csv_path)
        df = parser.process()
        df['execution_time_class'] = (df['elapsed_time'] > self.threshold).astype(int)
        # Prepare the X matrix
        X = df.drop(columns=['elapsed_time', 'execution_time_class'])
        # TODO: Feature prunning. Only keep features that does not occur overfitting.
        features = self.features or X.columns
        X = df[features]
        X = X.fillna(0)
        # Prepare the y vector
        y = df['execution_time_class']
        return X, y

    def split_data(self, X, y, ):
        X_train, X_temp, y_train, y_temp = train_test_split(
            X, y, test_size=self.test_size,
            random_state=self.random_state
        )
        X_val, X_test, y_val, y_test = train_test_split(
            X_temp, y_temp, test_size=self.valid_size_over_train,
            random_state=self.random_state,
        )
        return X_train, X_val, X_test, y_train, y_val, y_test

    def train_and_evaluate(self, X_train, y_train, X_test, y_test, verbose=False) -> dict:
        _print = print if verbose else lambda *args, **kwargs: None

        model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
        scores = cross_val_score(model, X_train, y_train, cv=5)
        _print(f"Cross-Validation Scores: {scores}")
        _print(f"CV Mean Score: {scores.mean():.2f}")

        start_time = time.time()
        model.fit(X_train, y_train)
        training_time = time.time() - start_time
        _print(f"Training Time: {training_time:.2f} seconds")

        start_time = time.time()
        predictions = model.predict(X_test)
        testing_time = time.time() - start_time
        accuracy = accuracy_score(y_test, predictions)
        _print(f"Model Accuracy: {accuracy:.2f}")

        stat = dict(
            training_time=training_time,
            testing_time=testing_time,
            accuracy=accuracy,
        )
        return stat


class SQLQueryClassifier:
    def __init__(
        self, csv_path, threshold=14000,
        test_size=0.4,
        valid_size_over_train=0.5,
        random_state=42,
    ):
        self.csv_path = csv_path
        self.threshold = threshold
        self.vectorizer = CountVectorizer()
        self.test_size = test_size
        self.valid_size_over_train = valid_size_over_train
        self.random_state = random_state

    def load_and_preprocess(self):
        df = pd.read_csv(self.csv_path)
        df['execution_time_class'] = (df['TOTAL_ELAPSED_TIME'] > self.threshold).astype(int)
        # print(df['execution_time_class'].value_counts())

        X = self.vectorizer.fit_transform(df['QUERY_TEXT'])
        y = df['execution_time_class']
        return X, y

    def split_data(self, X, y, ):
        X_train, X_temp, y_train, y_temp = train_test_split(
            X, y, test_size=self.test_size,
            random_state=self.random_state
        )
        X_val, X_test, y_val, y_test = train_test_split(
            X_temp, y_temp, test_size=self.valid_size_over_train,
            random_state=self.random_state,
        )
        return X_train, X_val, X_test, y_train, y_val, y_test

    def train_and_evaluate(self, X_train, y_train, X_test, y_test, verbose=False) -> dict:
        _print = print if verbose else lambda *args, **kwargs: None

        model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
        scores = cross_val_score(model, X_train, y_train, cv=5)
        _print(f"Cross-Validation Scores: {scores}")
        _print(f"CV Mean Score: {scores.mean():.2f}")

        start_time = time.time()
        model.fit(X_train, y_train)
        training_time = time.time() - start_time
        _print(f"Training Time: {training_time:.2f} seconds")

        start_time = time.time()
        predictions = model.predict(X_test)
        testing_time = time.time() - start_time
        accuracy = accuracy_score(y_test, predictions)
        _print(f"Model Accuracy: {accuracy:.2f}")

        stat = dict(
            training_time=training_time,
            testing_time=testing_time,
            accuracy=accuracy,
        )
        return stat


def main(csv_path, threshold, query_plan=False, verbose=False):
    if query_plan:
        classifier = SQLQueryPlanClassifier(
            csv_path, threshold=threshold,
            features=[],
        )
    else:
        classifier = SQLQueryClassifier(csv_path, threshold=threshold)
    X, y = classifier.load_and_preprocess()
    X_train, X_val, X_test, y_train, y_val, y_test = classifier.split_data(X, y)
    classifier.train_and_evaluate(X_train, y_train, X_test, y_test, verbose=verbose)
    return


def parse_args():
    parser = argparse.ArgumentParser(description="Train and evaluate a SQL query classifier.")
    parser.add_argument("csv_file", type=str, help="Path to the CSV file containing SQL queries.")
    parser.add_argument("query_plan", type=bool, default=False, help="If CSV file contains query plan data.")
    parser.add_argument("--threshold", type=int, default=15000, help="Threshold for classifying queries as slow.")
    parser.add_argument("--verbose", action="store_true", help="Print verbose output.")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    main(args.csv_file, args.threshold, query_plan=args.query_plan, verbose=args.verbose)
