"""
===============================================================================
Module: good_design.py

Path: module-1.1-software-design-oop/demos/demo-14-code-smells/good_design.py

Purpose:
Demonstrate how to eliminate common Code Smells by applying
Clean Code principles.

===============================================================================
"""

# Constants

NORMALIZATION_FACTOR = 40  # Defines the value used to normalize input data.

MODEL_THRESHOLD = 0.8  # Defines the classification decision threshold.

EXPECTED_PREDICTIONS = [0, 0, 1, 1]  # Defines the expected prediction results.


# Functions


def load_data():  # Responsible only for loading input data.
    """Return sample input data."""

    return [10, 20, 30, 40]  # Return raw dataset.


def normalize_data(data):  # Responsible only for data normalization.
    """Normalize input values."""

    return [value / NORMALIZATION_FACTOR for value in data]  # Return normalized values.


def train_model():  # Responsible only for model creation.
    """Create a simple model."""

    return {"threshold": MODEL_THRESHOLD}  # Return model configuration.


def generate_predictions(model, normalized_data):  # Responsible only for inference.
    """Generate predictions."""

    threshold = model["threshold"]  # Retrieve model threshold.

    return [
        1 if value > threshold else 0 for value in normalized_data
    ]  # Return predictions.


def evaluate_predictions(predictions):  # Responsible only for evaluation.
    """Calculate prediction accuracy."""

    correct_predictions = sum(
        prediction == expected
        for prediction, expected in zip(
            predictions,
            EXPECTED_PREDICTIONS,
        )
    )  # Count correct predictions.

    return correct_predictions / len(EXPECTED_PREDICTIONS)  # Return accuracy score.


def save_model(model):  # Responsible only for persistence.
    """Simulate saving the model."""

    print(f"Saving model: {model}")  # Display save operation.


def send_notification():  # Responsible only for notifications.
    """Simulate sending a notification."""

    print("Sending notification...")  # Display notification.


# Main


def main():  # Coordinates the complete ML workflow.
    """Program entry point."""

    raw_data = load_data()  # Load input data.

    normalized_data = normalize_data(raw_data)  # Normalize the data.

    model = train_model()  # Train the model.

    predictions = generate_predictions(
        model,
        normalized_data,
    )  # Generate predictions.

    accuracy = evaluate_predictions(predictions)  # Evaluate model performance.

    print(f"Data: {raw_data}")  # Display raw data.

    print(f"Processed: {normalized_data}")  # Display processed data.

    print(f"Model: {model}")  # Display model.

    print(f"Predictions: {predictions}")  # Display predictions.

    print(f"Accuracy: {accuracy}")  # Display evaluation metric.

    save_model(model)  # Save the model.

    send_notification()  # Notify completion.


# Entry Point

if __name__ == "__main__":  # Script entry point.
    main()  # Start the demonstration.
