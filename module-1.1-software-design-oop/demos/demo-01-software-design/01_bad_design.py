"""
Demo 01 - Bad Software Design

This example intentionally mixes multiple responsibilities
into a single function to illustrate poor software design.
"""


def main():
    # Load data
    data = [10, 20, 30, 40, 50]
    print(f"Loaded data: {data}")

    # Preprocess data
    normalized_data = [x / max(data) for x in data]
    print(f"Normalized data: {normalized_data}")

    # Train a fake model
    model = sum(normalized_data) / len(normalized_data)
    print(f"Model trained with value: {model:.2f}")

    # Make a prediction
    new_sample = 35 / max(data)
    prediction = model * new_sample

    # Display result
    print(f"Prediction: {prediction:.2f}")


if __name__ == "__main__":
    main()