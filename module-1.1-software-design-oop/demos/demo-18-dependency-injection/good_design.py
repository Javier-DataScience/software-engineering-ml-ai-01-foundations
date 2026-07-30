"""
Demo 18 - Dependency Injection

Good Design

This example demonstrates:
- Single Responsibility Principle (SRP)
- Composition
- Design by Interfaces
- Dependency Injection

The PredictionService does not create its own dependencies.
Instead, they are provided from the outside.
"""

# Imports

from abc import ABC, abstractmethod

# Interfaces


class ModelInterface(ABC):
    """Defines the contract that every ML model must implement."""

    @abstractmethod
    def predict(self, features: list[float]) -> int:
        """Generate a prediction."""
        

# Concrete Implementations


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


class XGBoostModel(ModelInterface):
    """Concrete implementation of an ML model."""

    def predict(self, features: list[float]) -> int:
        """Generate a fake prediction."""
        return 1


# Business Logic


class PredictionService:
    """Coordinates the prediction workflow."""

    def __init__(
        self,
        model: ModelInterface,
        logger: Logger,
        database: Database,
    ) -> None:
        # Receive the model instead of creating it.
        self.model = model

        # Receive the logger instead of creating it.
        self.logger = logger

        # Receive the database instead of creating it.
        self.database = database

    def predict(self, features: list[float]) -> int:
        """Execute the complete prediction workflow."""

        # Log the beginning of prediction.
        self.logger.log("Starting prediction...")

        # Ask the injected model to generate a prediction.
        prediction = self.model.predict(features)

        # Store the prediction.
        self.database.save_prediction(prediction)

        # Log completion.
        self.logger.log("Prediction completed.")

        return prediction


# Main


def main() -> None:
    """Create every dependency and inject them into the service."""

    # Create the concrete model.
    model = XGBoostModel()

    # Create the logger.
    logger = Logger()

    # Create the database.
    database = Database()

    # Inject every dependency into the service.
    prediction_service = PredictionService(
        model=model,
        logger=logger,
        database=database,
    )

    # Execute the prediction.
    prediction = prediction_service.predict([0.15, 0.42, 0.87])

    # Display the result.
    print(f"\nPrediction: {prediction}")


if __name__ == "__main__":
    main()
