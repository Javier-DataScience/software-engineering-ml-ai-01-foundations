"""
===============================================================================
Module: bad_design.py

Path:
module-1.1-software-design-oop/
demos/demo-17-design-interfaces/bad_design.py

Purpose:
Demonstrate a tightly coupled architecture where the prediction pipeline
depends directly on a concrete model implementation.

===============================================================================
"""


# Classes


class XGBoostModel:
    """Concrete ML model."""

    def predict(self, data):
        """Generate predictions."""

        return [1 if value > 0.5 else 0 for value in data]


class PredictionPipeline:
    """Prediction pipeline tightly coupled to XGBoost."""

    def __init__(self):
        """Create pipeline."""

        self.model = XGBoostModel()

    def run(self, data):
        """Execute prediction."""

        return self.model.predict(data)


# Main


def main():
    """Program entry point."""

    pipeline = PredictionPipeline()

    predictions = pipeline.run([0.3, 0.8, 0.9])

    print(f"Predictions: {predictions}")


# Entry Point


if __name__ == "__main__":
    main()
