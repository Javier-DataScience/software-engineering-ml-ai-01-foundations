"""
===============================================================================
Module: composition_design.py

Path:
module-1.1-software-design-oop/demos/demo-16-composition-vs-inheritance/
composition_design.py

Purpose:
Demonstrate an ML prediction pipeline implemented using composition.

===============================================================================
"""


# Classes


class MLModel:
    """Base machine learning model."""

    def predict(self, data):
        """Generate predictions."""

        return [1 if value > 15 else 0 for value in data]


class PredictionPipeline:
    """Prediction pipeline implemented using composition."""

    def __init__(self, model):
        """Receive a model through composition."""

        self.model = model

    def run(self):
        """Execute the prediction pipeline."""

        data = [10, 20, 30]

        predictions = self.model.predict(data)

        print(f"Predictions: {predictions}")


# Main


def main():
    """Program entry point."""

    model = MLModel()

    pipeline = PredictionPipeline(model)

    pipeline.run()


# Entry Point


if __name__ == "__main__":
    main()
