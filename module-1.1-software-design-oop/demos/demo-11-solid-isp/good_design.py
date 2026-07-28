"""
===============================================================================
Module: good_design.py

Path: module-1.1-software-design-oop/demos/demo-11-solid-isp/good_design.py

Purpose:
Demonstrate a correct implementation of the Interface Segregation Principle
(ISP) by splitting one large interface into several small, focused interfaces.

===============================================================================
"""

# Imports

from abc import ABC, abstractmethod  # Import tools for creating abstract classes.

# Classes


class Predictable(ABC):  # Define the prediction contract.
    """Interface for prediction services."""

    @abstractmethod  # Forces child classes to implement this method.
    def predict(self, data):  # Define the prediction behavior.
        """Generate predictions."""


class Trainable(ABC):  # Define the training contract.
    """Interface for trainable models."""

    @abstractmethod  # Forces child classes to implement this method.
    def train(self):  # Define the training behavior.
        """Train the model."""


class Evaluatable(ABC):  # Define the evaluation contract.
    """Interface for evaluation services."""

    @abstractmethod  # Forces child classes to implement this method.
    def evaluate(self):  # Define the evaluation behavior.
        """Evaluate the model."""


class Persistable(ABC):  # Define the persistence contract.
    """Interface for model persistence."""

    @abstractmethod  # Forces child classes to implement this method.
    def save(self):  # Define the save behavior.
        """Save the model."""

    @abstractmethod  # Forces child classes to implement this method.
    def load(self):  # Define the load behavior.
        """Load the model."""


class InferenceService(Predictable):  # Implements only the interface it needs.
    """Inference service."""

    def predict(self, data):  # Implement the prediction contract.
        return [
            1 if value > 15 else 0 for value in data
        ]  # Generate one prediction per sample.


# Functions


def run_inference(model, data):  # Client code that depends only on Predictable.
    """Run inference using any prediction service."""

    predictions = model.predict(data)  # Polymorphic call.

    print(f"Model: {model.__class__.__name__}")  # Display model name.
    print(f"Predictions: {predictions}")  # Display predictions.
    print(
        f"Number of predictions: {len(predictions)}"
    )  # Verify one prediction per sample.


# Main


def main():  # Coordinates the demonstration.
    """Program entry point."""

    data = [10, 20, 30]  # Sample input data.

    model = InferenceService()  # Create an inference service.

    run_inference(model, data)  # Execute prediction.


# Entry Point

if __name__ == "__main__":  # Script entry point.
    main()  # Start the demonstration.
