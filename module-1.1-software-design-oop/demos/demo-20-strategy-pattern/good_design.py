"""
Module:
    good_design.py

Path:
    module-1.1-software-design-oop/demos/demo-20-strategy-pattern/

Purpose:
    Demonstrate the Strategy Pattern for interchangeable ML models.

Responsibility:
    Define a flexible prediction workflow using model strategies.
"""

from abc import ABC, abstractmethod

# =============================================================================
# Strategy Interface
# =============================================================================


class ModelStrategy(ABC):
    """Define the contract for prediction strategies."""

    @abstractmethod
    def predict(self, features: list[float]) -> int:
        """Generate a prediction."""


# =============================================================================
# Concrete Strategies
# =============================================================================


class XGBoostStrategy(ModelStrategy):
    """Implement prediction using XGBoost."""

    def predict(self, features: list[float]) -> int:

        # Simulate XGBoost prediction.
        return 1


class LightGBMStrategy(ModelStrategy):
    """Implement prediction using LightGBM."""

    def predict(self, features: list[float]) -> int:

        # Simulate LightGBM prediction.
        return 0


class NeuralNetworkStrategy(ModelStrategy):
    """Implement prediction using a neural network."""

    def predict(self, features: list[float]) -> int:

        # Simulate neural network prediction.
        return 1


# =============================================================================
# Context
# =============================================================================


class PredictionPipeline:
    """Execute predictions using an injected strategy."""

    def __init__(self, strategy: ModelStrategy):

        # Store the selected prediction strategy.
        self.strategy = strategy

    def run(self, features: list[float]) -> int:

        # Delegate prediction to the selected strategy.
        return self.strategy.predict(features)


# =============================================================================
# Entry Point
# =============================================================================


if __name__ == "__main__":
    # Define input features.
    input_features = [10, 20, 30]

    # Create a specific prediction strategy.
    model_strategy = XGBoostStrategy()

    # Inject the strategy into the pipeline.
    pipeline = PredictionPipeline(model_strategy)

    # Execute prediction.
    prediction = pipeline.run(input_features)

    # Display prediction result.
    print("Prediction:", prediction)
