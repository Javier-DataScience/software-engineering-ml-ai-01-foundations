"""
===============================================================================
Module: good_design.py

Path: module-1.1-software-design-oop/demos/demo-15-cohesion-coupling/good_design.py

Purpose:
Demonstrate high cohesion and low coupling by separating responsibilities
into specialized classes and depending on abstractions.

===============================================================================
"""

# Imports

from abc import ABC, abstractmethod  # Import tools for creating abstract classes.

# Classes


class MLModel(ABC):
    """Abstract contract for all machine learning models."""

    @abstractmethod  # Forces every child class to implement this method.
    def predict(self, data):
        """Generate predictions."""


class RandomForestModel(MLModel):
    """Random Forest implementation."""

    def predict(self, data):
        """Generate predictions."""

        return [1 if value > 15 else 0 for value in data]


class DataLoader:
    """Responsible only for loading data."""

    def load_data(self):
        """Return sample data."""

        return [10, 20, 30]


class ModelTrainer:
    """Responsible only for inference."""

    def __init__(self, model):
        """Receive any MLModel implementation."""

        self.model = model  # Low coupling through dependency injection.

    def generate_predictions(self, data):
        """Generate predictions."""

        return self.model.predict(data)


class ModelEvaluator:
    """Responsible only for evaluation."""

    def evaluate(self, predictions):
        """Calculate prediction accuracy."""

        expected_predictions = [0, 1, 1]  # Expected results.

        correct_predictions = sum(
            prediction == expected
            for prediction, expected in zip(
                predictions,
                expected_predictions,
            )
        )

        return correct_predictions / len(expected_predictions)


class DeploymentService:
    """Responsible only for deployment."""

    def deploy(self):
        """Simulate deployment."""

        print("Deploying model...")


class NotificationService:
    """Responsible only for notifications."""

    def notify(self):
        """Simulate notification."""

        print("Sending notification...")


# Main


def main():
    """Program entry point."""

    data_loader = DataLoader()  # Create data loader.

    model = RandomForestModel()  # Create model.

    trainer = ModelTrainer(model)  # Inject dependency.

    evaluator = ModelEvaluator()  # Create evaluator.

    deployment = DeploymentService()  # Create deployment service.

    notification = NotificationService()  # Create notification service.

    data = data_loader.load_data()  # Load data.

    predictions = trainer.generate_predictions(data)  # Generate predictions.

    accuracy = evaluator.evaluate(predictions)  # Evaluate predictions.

    deployment.deploy()  # Deploy model.

    notification.notify()  # Notify completion.

    print(f"Predictions: {predictions}")  # Display predictions.

    print(f"Accuracy: {accuracy}")  # Display evaluation result.


# Entry Point


if __name__ == "__main__":
    """Script entry point."""

    main()
