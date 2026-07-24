"""
Demo 01 - Improved Software Design

This example separates responsibilities into small,
focused functions while preserving the same behavior.
"""


def load_data():
    """Load the dataset."""
    return [10, 20, 30, 40, 50]


def preprocess_data(data):
    """Normalize the dataset."""
    return [x / max(data) for x in data]


def train_model(data):
    """Train a simple model."""
    return sum(data) / len(data)


def predict(model, sample):
    """Generate a prediction."""
    return model * sample


def display_results(data, normalized_data, model, prediction):
    """Display the results."""
    print(f"Loaded data: {data}")
    print(f"Normalized data: {normalized_data}")
    print(f"Model trained with value: {model:.2f}")
    print(f"Prediction: {prediction:.2f}")


def main():
    data = load_data()
    normalized_data = preprocess_data(data)
    model = train_model(normalized_data)

    sample = 35 / max(data)
    prediction = predict(model, sample)

    display_results(data, normalized_data, model, prediction)


if __name__ == "__main__":
    main()