import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
from collections import Counter
import sys

class SQLQueryPerformanceClassifier:
    def __init__(self, csv_path, threshold=14000):
        self.csv_path = csv_path
        self.threshold = threshold
        self.vectorizer = CountVectorizer()

    def load_and_prepare_data(self):
        self.df = pd.read_csv(self.csv_path)
        X = self.vectorizer.fit_transform(self.df['QUERY_TEXT'])
        y = self.df['TOTAL_ELAPSED_TIME']
        return X, y

    def split_data(self, X, y):
        return train_test_split(X, y, test_size=0.2, random_state=42)

    def train_model(self, X_train, y_train):
        self.model = LinearRegression()
        self.model.fit(X_train, y_train)

    def predict_and_evaluate(self, X_test, y_test):
        predicted_times = self.model.predict(X_test)
        mse = mean_squared_error(y_test, predicted_times)
        rmse = np.sqrt(mse)
        print(f"Model RMSE: {rmse}")
        return predicted_times

    def classify_queries(self, predicted_times):
        classified_predictions = ['long-running' if time > self.threshold else 'short-running' for time in predicted_times]
        classification_counts = Counter(classified_predictions)
        print(classification_counts)

def main(csv_path):
    classifier = SQLQueryPerformanceClassifier(csv_path)
    X, y = classifier.load_and_prepare_data()
    X_train, X_test, y_train, y_test = classifier.split_data(X, y)
    classifier.train_model(X_train, y_train)
    predicted_times = classifier.predict_and_evaluate(X_test, y_test)
    classifier.classify_queries(predicted_times)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <path_to_csv_file>")
        sys.exit(1)
    csv_path = sys.argv[1]
    main(csv_path)
