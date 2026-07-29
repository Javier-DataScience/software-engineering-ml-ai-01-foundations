"""
===============================================================================
Module: inheritance_design.py

Path:
module-1.1-software-design-oop/demos/demo-16-composition-vs-inheritance/
inheritance_design.py

Purpose:
Demonstrate an ML prediction pipeline implemented using inheritance.

===============================================================================
"""


# Classes


class MLModel:
    """Base machine learning model."""

    def predict(self, data):
        """Generate predictions."""

        return [1 if value > 15 else 0 for value in data]


class PredictionPipeline(MLModel):
    """Prediction pipeline implemented through inheritance."""

    def run(self):
        """Execute the prediction pipeline."""

        data = [10, 20, 30]

        predictions = self.predict(data)

        print(f"Predictions: {predictions}")


# Main


def main():
    """Program entry point."""

    pipeline = PredictionPipeline()

    pipeline.run()


# Entry Point


if __name__ == "__main__":
    main()
