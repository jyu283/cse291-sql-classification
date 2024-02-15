import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split, cross_val_score
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
import time
import sys

class SQLQueryClassifier:
    def __init__(self, csv_path, threshold=14000):
        self.csv_path = csv_path
        self.threshold = threshold
        self.vectorizer = CountVectorizer()

    def load_and_preprocess(self):
        df = pd.read_csv(self.csv_path)
        df['execution_time_class'] = (df['TOTAL_ELAPSED_TIME'] > self.threshold).astype(int)
        print(df['execution_time_class'].value_counts())

        X = self.vectorizer.fit_transform(df['QUERY_TEXT'])
        y = df['execution_time_class']
        return X, y

    def split_data(self, X, y):
        X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.2, random_state=42)
        X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
        return X_train, X_val, X_test, y_train, y_val, y_test

    def train_and_evaluate(self, X_train, y_train, X_test, y_test):
        model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
        scores = cross_val_score(model, X_train, y_train, cv=5)
        print(f"Cross-Validation Scores: {scores}")
        print(f"CV Mean Score: {scores.mean():.2f}")

        start_time = time.time()
        model.fit(X_train, y_train)
        training_time = time.time() - start_time
        print(f"Training Time: {training_time:.2f} seconds")

        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        print(f"Model Accuracy: {accuracy:.2f}")

def main(csv_path):
    classifier = SQLQueryClassifier(csv_path)
    X, y = classifier.load_and_preprocess()
    X_train, X_val, X_test, y_train, y_val, y_test = classifier.split_data(X, y)
    classifier.train_and_evaluate(X_train, y_train, X_test, y_test)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <path_to_csv_file>")
        sys.exit(1)
    csv_path = sys.argv[1]
    main(csv_path)
