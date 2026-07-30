"""
Demo 18 - Dependency Injection

Bad Design

The PredictionService creates every dependency itself.

Problems:
- High coupling
- Difficult to test
- Difficult to replace implementations
- Violates Dependency Injection
- Violates Dependency Inversion Principle
"""

# Classes


class Logger:
    """Writes messages to the console."""

    def log(self, message: str) -> None:
        """Print a log message."""
        print(f"[LOG] {message}")


class Database:
    """Simulates a database."""

    def save_prediction(self, prediction: int) -> None:
        """Store a prediction."""
        print(f"Saving prediction {prediction} into the database.")


class XGBoostModel:
    """Concrete ML model."""

    def predict(self, features: list[float]) -> int:
        """Return a fake prediction."""
        return 1


class PredictionService:
    """Coordinates the prediction workflow."""

    def __init__(self) -> None:
        # BAD:
        # The service creates every dependency itself.
        self.logger = Logger()
        self.database = Database()
        self.model = XGBoostModel()

    def predict(self, features: list[float]) -> int:
        """Execute the prediction workflow."""

        # Log the beginning of prediction.
        self.logger.log("Starting prediction...")

        # Ask the model to predict.
        prediction = self.model.predict(features)

        # Store the prediction.
        self.database.save_prediction(prediction)

        # Log completion.
        self.logger.log("Prediction completed.")

        return prediction


# Main


def main() -> None:
    """Run the bad design example."""

    service = PredictionService()

    prediction = service.predict([0.1, 0.5, 0.8])

    print(f"\nPrediction: {prediction}")


if __name__ == "__main__":
    main()
