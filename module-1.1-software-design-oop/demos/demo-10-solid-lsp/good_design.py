"""
===============================================================================
Module: good_design.py

Path: module-1.1-software-design-oop/demos/demo-10-solid-lsp/good_design.py

Purpose:
Demonstrate a correct implementation of the Liskov Substitution Principle (LSP)
using inheritance, abstraction, and polymorphism.

===============================================================================
"""

# Imports

from abc import ABC, abstractmethod  # Import tools for creating abstract classes.

# Classes

class MLModel(ABC):
    """Abstract base class defining the common contract."""

    @abstractmethod  # Forces every child class to implement this method.
    def predict(self, data):  # Defines the common behavior shared by all ML models.
        """Return a list of predictions."""


class RandomForestModel(MLModel):  # Inherits the contract from MLModel.
    """Random Forest implementation."""

    def predict(self, data):  # Provides its own implementation of the contract.
        return [1 for _ in data]  # Returns one prediction per input sample.


class XGBoostModel(MLModel):  # Inherits the contract from MLModel.
    """XGBoost implementation."""

    def predict(self, data):  # Provides its own implementation of the contract.
        return [0 for _ in data]  # Returns one prediction per input sample.


class NeuralNetworkModel(MLModel):  # Inherits the contract from MLModel.
    """Neural Network implementation."""

    def predict(self, data):  # Provides its own implementation of the contract.
        return [1 if value > 15 else 0 for value in data]  # Applies a simple prediction rule.


# Functions

def evaluate_model(model, data):  # Client code that works with any MLModel object.
    """Evaluate any MLModel."""

    predictions = model.predict(data)  # Polymorphic call.

    print(f"Model: {model.__class__.__name__}")  # Display model name.
    print(f"Predictions: {predictions}")  # Display predictions.
    print(f"Number of predictions: {len(predictions)}")  # Verify contract.
    print("-" * 40)  # Console separator.


# Main

def main():  # Coordinates the execution of the demonstration.
    """Program entry point."""

    data = [10, 20, 30]  # Sample input data.

    models = [  # Different MLModel implementations.
        RandomForestModel(),  # Random Forest model.
        XGBoostModel(),  # XGBoost model.
        NeuralNetworkModel(),  # Neural Network model.
    ]

    for model in models:  # Evaluate every model.
        evaluate_model(model, data)  # Demonstrates LSP and polymorphism.


# Entry Point

if __name__ == "__main__":  # Script entry point.
    main()  # Start the demonstration.