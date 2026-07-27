
"""
===============================================================================
Module: good_design.py

Path: module-1.1-software-design-oop/demos/demo-12-solid-dip/good_design.py

Purpose:
Demonstrate a correct implementation of the Dependency Inversion Principle
(DIP) using abstraction, polymorphism, and constructor dependency injection.

===============================================================================
"""

# Imports

from abc import ABC, abstractmethod  # Import tools for creating abstract classes.


# Classes

class Predictable(ABC):
    """Abstract prediction contract."""

    @abstractmethod  # Force child classes to implement this method.
    def predict(self, data):  # Define the prediction behavior.
        """Generate predictions."""


class RandomForestModel(Predictable):  # Implements the prediction contract.
    """Random Forest implementation."""

    def predict(self, data):  # Implement the prediction behavior.
        return [1 if value > 15 else 0 for value in data]  # Simple prediction rule.


class XGBoostModel(Predictable):  # Implements the prediction contract.
    """XGBoost implementation."""

    def predict(self, data):  # Implement the prediction behavior.
        return [0 if value > 15 else 1 for value in data]  # Different prediction rule.


class PredictionService:
    """High-level service depending only on an abstraction."""

    def __init__(self, model):  # Receive the dependency from outside.
        self.model = model  # Store any Predictable implementation.

    def predict(self, data):  # Delegate prediction to the injected model.
        return self.model.predict(data)  # Polymorphic call.


# Main

def main():  # Coordinates the demonstration.
    """Program entry point."""

    data = [10, 20, 30]  # Sample input data.

    model = RandomForestModel()  # Create the desired implementation.

    service = PredictionService(model)  # Inject the dependency.

    predictions = service.predict(data)  # Perform predictions.

    print(f"Service: {service.__class__.__name__}")  # Display service name.
    print(f"Injected Model: {service.model.__class__.__name__}")  # Display injected model.
    print(f"Predictions: {predictions}")  # Display predictions.

    print("\nReplacing the model...\n")  # Demonstrate flexibility.

    model = XGBoostModel()  # Create another implementation.

    service = PredictionService(model)  # Inject the new dependency.

    predictions = service.predict(data)  # Perform predictions again.

    print(f"Service: {service.__class__.__name__}")  # Display service name.
    print(f"Injected Model: {service.model.__class__.__name__}")  # Display injected model.
    print(f"Predictions: {predictions}")  # Display predictions.


# Entry Point

if __name__ == "__main__":  # Script entry point.
    main()  # Start the demonstration.
