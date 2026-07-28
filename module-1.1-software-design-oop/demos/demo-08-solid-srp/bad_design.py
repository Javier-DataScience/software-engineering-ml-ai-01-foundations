"""
===============================================================================
Module: bad_design.py

Path: module-1.1-software-design-oop/demos/demo-08-solid-srp/bad_design.py

Purpose:
Demonstrate an incorrect implementation of the Single Responsibility Principle
(SRP), where one class is responsible for multiple independent tasks.

===============================================================================
"""


class MLPipeline:
    """Pipeline that violates SRP."""

    def load_data(self):  # Load the dataset.
        print("Loading data...")

    def preprocess_data(self):  # Transform the dataset.
        print("Preprocessing data...")

    def train_model(self):  # Train the ML model.
        print("Training model...")

    def evaluate_model(self):  # Evaluate model performance.
        print("Evaluating model...")

    def save_model(self):  # Save the trained model.
        print("Saving model...")


def main():  # Coordinates the demonstration.
    """Program entry point."""

    pipeline = MLPipeline()

    pipeline.load_data()
    pipeline.preprocess_data()
    pipeline.train_model()
    pipeline.evaluate_model()
    pipeline.save_model()


if __name__ == "__main__":  # Script entry point.
    main()
