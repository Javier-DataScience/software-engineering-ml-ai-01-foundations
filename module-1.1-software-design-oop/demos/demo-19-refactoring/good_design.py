"""
PEP:
    - PEP 8: Style Guide for Python Code
    - PEP 257: Docstring Conventions

Module:
    Phase 1 → Module 1.1 → Demo 19
    File: good_design.py

Purpose:
    Refactor the prediction pipeline without changing its external behavior.
"""

# =============================================================================
# Constants
# =============================================================================

NORMALIZATION_FACTOR = 40
PREDICTION_THRESHOLD = 0.8

# =============================================================================
# Functions
# =============================================================================


def normalize_data(values: list[float]) -> list[float]:
    """Normalize feature values."""

    # Normalize every feature using the predefined normalization factor.
    return [value / NORMALIZATION_FACTOR for value in values]


def generate_predictions(
    normalized_values: list[float],
) -> list[int]:
    """Generate predictions from normalized values."""

    predictions = []

    # Generate predictions using the configured threshold.
    for value in normalized_values:
        if value > PREDICTION_THRESHOLD:
            predictions.append(1)
        else:
            predictions.append(0)

    return predictions


def run_pipeline() -> None:
    """Execute the complete ML prediction pipeline."""

    # Define the input features.
    features = [10, 20, 30, 40]

    # Normalize the input data.
    normalized_features = normalize_data(features)

    # Generate predictions.
    predictions = generate_predictions(normalized_features)

    # Display the predictions.
    print("Predictions:", predictions)


# =============================================================================
# Entry Point
# =============================================================================

if __name__ == "__main__":
    # Execute the ML workflow.
    run_pipeline()
