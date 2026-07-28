"""
===============================================================================
Module: bad_design.py

Path: module-1.1-software-design-oop/demos/demo-15-cohesion-coupling/bad_design.py

Purpose:
Demonstrate low cohesion and high coupling using a simple ML system.

===============================================================================
"""


# Classes


class RandomForestModel:
    """Concrete model implementation."""

    def predict(self, data):
        """Generate predictions."""

        return [1 if value > 15 else 0 for value in data]


class MLSystem:
    """A class with multiple unrelated responsibilities."""

    def __init__(self):
        """Initialize the ML system."""

        self.model = RandomForestModel()  # High coupling: concrete dependency.

    def run_pipeline(self):
        """Execute the complete ML workflow."""

        # Load data.
        data = [10, 20, 30]

        # Generate predictions.
        predictions = self.model.predict(data)

        # Evaluate predictions.
        accuracy = (
            sum(
                prediction == expected
                for prediction, expected in zip(
                    predictions,
                    [0, 1, 1],
                )
            )
            / 3
        )

        # Deploy model.
        print("Deploying model...")

        # Notify completion.
        print("Sending notification...")

        print(f"Predictions: {predictions}")
        print(f"Accuracy: {accuracy}")


# Main


def main():
    """Program entry point."""

    system = MLSystem()

    system.run_pipeline()


# Entry Point


if __name__ == "__main__":
    main()
