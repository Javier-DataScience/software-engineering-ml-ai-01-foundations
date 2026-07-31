"""
Module:
    bad_design.py

Path:
    module-1.1-software-design-oop/demos/demo-20-strategy-pattern/

Purpose:
    Demonstrate a tightly coupled ML prediction pipeline.

Responsibility:
    Show the problems solved by the Strategy Pattern.
"""


# =============================================================================
# Models
# =============================================================================


class XGBoostModel:
    """Simulate an XGBoost prediction model."""

    def predict(self, features: list[float]) -> int:
        # Return a simulated prediction.
        return 1


class LightGBMModel:
    """Simulate a LightGBM prediction model."""

    def predict(self, features: list[float]) -> int:
        # Return a simulated prediction.
        return 0


class NeuralNetworkModel:
    """Simulate a neural network prediction model."""

    def predict(self, features: list[float]) -> int:
        # Return a simulated prediction.
        return 1


# =============================================================================
# Pipeline
# =============================================================================


class PredictionPipeline:
    """Execute predictions using different models."""

    def run(
        self,
        model_type: str,
        features: list[float],
    ) -> int:
        # Select the model depending on the received type.
        if model_type == "xgboost":
            # Create XGBoost model.
            model = XGBoostModel()

        elif model_type == "lightgbm":
            # Create LightGBM model.
            model = LightGBMModel()

        elif model_type == "neural_network":
            # Create Neural Network model.
            model = NeuralNetworkModel()

        else:
            # Raise error for unsupported models.
            raise ValueError("Unsupported model type.")

        # Execute prediction.
        return model.predict(features)


# =============================================================================
# Entry Point
# =============================================================================

if __name__ == "__main__":
    # Define input features.
    input_features = [10, 20, 30]

    # Create prediction pipeline.
    pipeline = PredictionPipeline()

    # Execute prediction.
    prediction = pipeline.run(
        "xgboost",
        input_features,
    )

    # Display prediction result.
    print("Prediction:", prediction)
