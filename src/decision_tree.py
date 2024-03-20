import argparse

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split, cross_val_score
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
import time


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


def main(csv_path, threshold):
    classifier = SQLQueryClassifier(csv_path, threshold=threshold)
    X, y = classifier.load_and_preprocess()
    X_train, X_val, X_test, y_train, y_val, y_test = classifier.split_data(X, y)
    classifier.train_and_evaluate(X_train, y_train, X_test, y_test)


def parse_args():
    parser = argparse.ArgumentParser(description="Train and evaluate a SQL query classifier.")
    parser.add_argument("csv_file", type=str, help="Path to the CSV file containing SQL queries.")
    parser.add_argument("--threshold", type=int, default=15000, help="Threshold for classifying queries as slow.")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    main(args.csv_file, args.threshold)
