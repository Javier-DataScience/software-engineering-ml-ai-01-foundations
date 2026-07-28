"""
===============================================================================
Module: bad_design.py

Path: module-1.1-software-design-oop/demos/demo-11-solid-isp/bad_design.py

Purpose:
Demonstrate an incorrect implementation of the Interface Segregation Principle
(ISP), where one large interface forces classes to implement methods they do
not need.

===============================================================================
"""

# Imports

from abc import ABC, abstractmethod  # Import tools for creating abstract classes.

# Classes


class MLComponent(ABC):
    """Large interface that violates ISP."""

    @abstractmethod  # Force child classes to implement this method.
    def train(self):  # Define the training contract.
        """Train the model."""

    @abstractmethod  # Force child classes to implement this method.
    def predict(self, data):  # Define the prediction contract.
        """Generate predictions."""

    @abstractmethod  # Force child classes to implement this method.
    def evaluate(self):  # Define the evaluation contract.
        """Evaluate the model."""

    @abstractmethod  # Force child classes to implement this method.
    def save(self):  # Define the persistence contract.
        """Save the model."""

    @abstractmethod  # Force child classes to implement this method.
    def load(self):  # Define the loading contract.
        """Load the model."""


class InferenceService(MLComponent):  # Implements the entire interface.
    """Inference service that violates ISP."""

    def train(self):  # Forced to implement an unnecessary method.
        raise NotImplementedError("InferenceService cannot train models.")

    def predict(self, data):  # The only behavior this class actually needs.
        return [1 if value > 15 else 0 for value in data]

    def evaluate(self):  # Forced to implement an unnecessary method.
        raise NotImplementedError("InferenceService cannot evaluate models.")

    def save(self):  # Forced to implement an unnecessary method.
        raise NotImplementedError("InferenceService cannot save models.")

    def load(self):  # Forced to implement an unnecessary method.
        raise NotImplementedError("InferenceService cannot load models.")


# Functions


def run_inference(model, data):  # Client code that only needs predictions.
    """Run inference using any ML component."""

    predictions = model.predict(data)  # Only prediction is required.

    print(f"Model: {model.__class__.__name__}")  # Display model name.
    print(f"Predictions: {predictions}")  # Display predictions.


# Main


def main():  # Coordinates the demonstration.
    """Program entry point."""

    data = [10, 20, 30]  # Sample input data.

    model = InferenceService()  # Create an inference service.

    run_inference(model, data)  # Prediction works correctly.

    print("\nTrying to train the inference service...\n")

    model.train()  # ISP violation becomes evident.


# Entry Point

if __name__ == "__main__":  # Script entry point.
    main()  # Start the demonstration.
