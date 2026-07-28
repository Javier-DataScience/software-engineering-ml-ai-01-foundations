"""
===============================================================================
Module: good_design.py

Path: module-1.1-software-design-oop/demos/demo-13-clean-code/good_design.py

Purpose:
Demonstrate Clean Code principles by refactoring an ML pipeline into
small, focused, and maintainable components.

===============================================================================
"""


# Constants

NORMALIZATION_FACTOR = 40  # Defines the value used to normalize input data.

MODEL_THRESHOLD = 0.8  # Defines the classification decision threshold.

EXPECTED_RESULTS = [0, 0, 1, 1]  # Defines expected predictions for evaluation.


# Functions


def load_data():  # Responsible only for loading input data.
    """Load raw input data."""

    return [10, 20, 30, 40]  # Return sample dataset.


def preprocess_data(data):  # Responsible only for data transformation.
    """Normalize input data."""

    return [value / NORMALIZATION_FACTOR for value in data]  # Return normalized values.


def train_model():  # Responsible only for model creation.
    """Create and return a simple trained model."""

    return {"threshold": MODEL_THRESHOLD}  # Return trained model representation.


def generate_predictions(model, processed_data):  # Responsible only for inference.
    """Generate predictions using the model."""

    threshold = model["threshold"]  # Extract decision threshold.

    return [
        1 if value > threshold else 0 for value in processed_data
    ]  # Return predictions.


def evaluate_predictions(
    predictions, expected_results
):  # Responsible only for evaluation.
    """Calculate model accuracy."""

    correct_predictions = sum(
        prediction == expected
        for prediction, expected in zip(predictions, expected_results)
    )  # Count correct predictions.

    return correct_predictions / len(expected_results)  # Return accuracy score.


def save_model(model):  # Responsible only for model persistence.
    """Simulate saving the model."""

    print(f"Saving model: {model}")  # Display saved model.


# Main


def main():  # Coordinates the ML pipeline execution.
    """Program entry point."""

    data = load_data()  # Load raw data.

    processed_data = preprocess_data(data)  # Transform data.

    model = train_model()  # Train model.

    predictions = generate_predictions(model, processed_data)  # Generate predictions.

    accuracy = evaluate_predictions(
        predictions, EXPECTED_RESULTS
    )  # Evaluate model performance.

    print(f"Model: {model}")  # Display model.

    print(f"Predictions: {predictions}")  # Display predictions.

    print(f"Accuracy: {accuracy}")  # Display evaluation result.

    save_model(model)  # Save model.


# Entry Point

if __name__ == "__main__":  # Script entry point.
    main()  # Start the demonstration.
