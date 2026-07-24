class MLPipeline:
    """A class that violates the Single Responsibility Principle."""

    def load_data(self):
        print("Loading data...")

    def preprocess_data(self):
        print("Preprocessing data...")

    def train_model(self):
        print("Training model...")

    def evaluate_model(self):
        print("Evaluating model...")

    def save_model(self):
        print("Saving model...")


def main():

    pipeline = MLPipeline()

    pipeline.load_data()
    pipeline.preprocess_data()
    pipeline.train_model()
    pipeline.evaluate_model()
    pipeline.save_model()


if __name__ == "__main__":
    main()