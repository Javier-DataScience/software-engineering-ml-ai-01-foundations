class DataLoader:

    def load_data(self):
        print("Loading data...")


class Preprocessor:

    def preprocess_data(self):
        print("Preprocessing data...")


class ModelTrainer:

    def train_model(self):
        print("Training model...")


class ModelEvaluator:

    def evaluate_model(self):
        print("Evaluating model...")


class ModelRepository:

    def save_model(self):
        print("Saving model...")


def main():

    loader = DataLoader()
    preprocessor = Preprocessor()
    trainer = ModelTrainer()
    evaluator = ModelEvaluator()
    repository = ModelRepository()

    loader.load_data()
    preprocessor.preprocess_data()
    trainer.train_model()
    evaluator.evaluate_model()
    repository.save_model()


if __name__ == "__main__":
    main()