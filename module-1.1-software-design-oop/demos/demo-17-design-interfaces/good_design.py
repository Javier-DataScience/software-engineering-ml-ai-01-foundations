"""
===============================================================================
Module: good_design.py

Path:
module-1.1-software-design-oop/
demos/demo-17-design-interfaces/good_design.py

Purpose:
Demonstrate interface-based design by making the prediction pipeline
depend on an abstraction instead of a concrete ML model.

===============================================================================
"""

# Imports

# Import tools for creating abstract interfaces.
from abc import ABC, abstractmethod

# Classes


class ModelInterface(ABC):  # Define the contract that every ML model must satisfy.
    """Define the contract for all ML models."""

    @abstractmethod
    def predict(self, data):  # Force subclasses to implement prediction.
        """Generate predictions."""


class XGBoostModel(ModelInterface):  # Concrete implementation of the model interface.
    """Concrete implementation of the model interface."""

    def predict(self, data):  # Generate predictions using the concrete model.
        """Generate predictions."""

        return [1 if value > 0.5 else 0 for value in data]  # Return predicted labels.


class PredictionPipeline:  # Coordinate the prediction workflow.
    """Prediction pipeline depending on an abstraction."""

    def __init__(self, model):  # Receive any object implementing the interface.
        """Initialize the prediction pipeline."""

        self.model = model  # Store the injected model.

    def run(self, data):  # Execute the prediction workflow.
        """Run the prediction pipeline."""

        return self.model.predict(data)  # Delegate prediction to the model.


# Main


def main():  # Demonstrate the interface-based architecture.
    """Program entry point."""

    model = XGBoostModel()  # Create a concrete model implementation.

    pipeline = PredictionPipeline(model)  # Inject the model into the pipeline.

    predictions = pipeline.run([0.3, 0.8, 0.9])  # Execute predictions.

    print(f"Predictions: {predictions}")  # Display prediction results.


# Entry Point


if __name__ == "__main__":  # Execute the demo when run as a script.
    main()  # Start the demonstration.
