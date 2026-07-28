"""
===============================================================================
Module: bad_design.py

Path: module-1.1-software-design-oop/demos/demo-12-solid-dip/bad_design.py

Purpose:
Demonstrate an incorrect implementation of the Dependency Inversion Principle
(DIP), where a high-level module depends directly on a concrete model
implementation.

===============================================================================
"""

# Classes


class RandomForestModel:
    """Concrete Random Forest implementation."""

    def predict(self, data):  # Generate predictions.
        return [1 if value > 15 else 0 for value in data]  # Simple prediction rule.


class PredictionService:
    """High-level service tightly coupled to RandomForestModel."""

    def __init__(self):  # Initialize the prediction service.
        self.model = RandomForestModel()  # Direct dependency (DIP violation).

    def predict(self, data):  # Delegate prediction to the model.
        return self.model.predict(data)  # Forward prediction request.


# Main


def main():  # Coordinates the demonstration.
    """Program entry point."""

    data = [10, 20, 30]  # Sample input data.

    service = PredictionService()  # Create the prediction service.

    predictions = service.predict(data)  # Perform predictions.

    print(f"Service: {service.__class__.__name__}")  # Display service name.
    print(f"Model: {service.model.__class__.__name__}")  # Display concrete model.
    print(f"Predictions: {predictions}")  # Display predictions.


# Entry Point

if __name__ == "__main__":  # Script entry point.
    main()  # Start the demonstration.
