"""
===============================================================================
Module: good_design.py

Path: module-1.1-software-design-oop/demos/demo-08-solid-srp/good_design.py

Purpose:
Demonstrate a correct implementation of the Single Responsibility Principle
(SRP), where each class has one well-defined responsibility.

===============================================================================
"""


class DataLoader:
    """Responsible for loading data."""

    def load_data(self):  # Load the dataset.
        print("Loading data...")


class Preprocessor:
    """Responsible for preprocessing data."""

    def preprocess_data(self):  # Transform the dataset.
        print("Preprocessing data...")


class ModelTrainer:
    """Responsible for training the model."""

    def train_model(self):  # Train the ML model.
        print("Training model...")


class ModelEvaluator:
    """Responsible for evaluating the model."""

    def evaluate_model(self):  # Evaluate model performance.
        print("Evaluating model...")


class ModelRepository:
    """Responsible for persisting the model."""

    def save_model(self):  # Save the trained model.
        print("Saving model...")


def main():  # Coordinates the workflow.
    """Program entry point."""

    loader = DataLoader()
    preprocessor = Preprocessor()
    trainer = ModelTrainer()
    evaluator = ModelEvaluator()
    repository = ModelRepository()

    loader.load_data()
    preprocessor.preprocess_data()
    trainer.train_model()
    evaluator.evaluate_model()
    repository.save_model()


if __name__ == "__main__":  # Script entry point.
    main()
