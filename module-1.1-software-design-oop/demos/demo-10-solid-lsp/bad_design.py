"""
===============================================================================
Module: bad_design.py

Path: module-1.1-software-design-oop/demos/demo-10-solid-lsp/bad_design.py

Purpose:
Demonstrate an incorrect implementation of the Liskov Substitution Principle
(LSP), where a child class violates the behavioral contract defined by its
parent class.

===============================================================================
"""


class MLModel:
    """Parent class defining the common prediction contract."""

    def predict(self, data):  # Common prediction interface.
        raise NotImplementedError  # Child classes must implement this method.


class RandomForestModel(MLModel):  # Correct MLModel implementation.
    """Random Forest model."""

    def predict(self, data):  # Respects the parent contract.
        return [1 for _ in data]  # Returns one prediction per sample.


class BrokenModel(MLModel):  # Incorrect MLModel implementation.
    """Broken model that violates LSP."""

    def predict(self, data):  # Violates the parent contract.
        return None  # Should return a list, not None.


def evaluate_model(model, data):  # Works with any MLModel.
    """Evaluate an ML model."""

    predictions = model.predict(data)  # Polymorphic call.

    print(f"Model: {model.__class__.__name__}")
    print(f"Predictions: {predictions}")

    # The client assumes every model returns a list.
    print(f"Number of predictions: {len(predictions)}")


def main():  # Coordinates the demonstration.
    """Program entry point."""

    data = [10, 20, 30]  # Sample input data.

    print("Random Forest")
    evaluate_model(RandomForestModel(), data)

    print("\nBroken Model")
    evaluate_model(BrokenModel(), data)  # This line raises an exception.


if __name__ == "__main__":  # Script entry point.
    main()
