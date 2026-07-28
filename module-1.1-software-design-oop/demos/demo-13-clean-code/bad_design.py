"""
===============================================================================
Module: bad_design.py

Path: module-1.1-software-design-oop/demos/demo-13-clean-code/bad_design.py

Purpose:
Demonstrate common Clean Code violations using a poorly structured ML pipeline.

===============================================================================
"""

# Functions


def train_pipeline():  # A single function that handles multiple responsibilities.

    data = [10, 20, 30, 40]  # Raw input data.

    x = []  # Poor variable name. The purpose of this list is unclear.

    for i in data:  # Process every input value.
        x.append(i / 40)  # Magic number and unclear transformation logic.

    model = {}  # Simulates a trained model.

    model["threshold"] = 0.8  # Magic number without explanation.

    predictions = []  # Stores model predictions.

    for value in x:  # Generate predictions.
        if value > model["threshold"]:  # Apply prediction rule.
            predictions.append(1)  # Positive prediction.
        else:
            predictions.append(0)  # Negative prediction.

    correct = 0  # Counter for correct predictions.

    expected = [0, 0, 1, 1]  # Expected results.

    for i in range(len(predictions)):  # Compare predictions with expected values.
        if predictions[i] == expected[i]:  # Check if prediction is correct.
            correct += 1  # Increase correct counter.

    accuracy = correct / len(expected)  # Calculate accuracy.

    print("Model:", model)  # Display trained model.

    print("Predictions:", predictions)  # Display predictions.

    print("Accuracy:", accuracy)  # Display evaluation result.

    print("Saving model...")  # Simulate model persistence.


# Main


def main():  # Program entry point.

    train_pipeline()  # Execute the complete ML pipeline.


# Entry Point

if __name__ == "__main__":  # Script entry point.
    main()  # Start the demonstration.
