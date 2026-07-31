# 1. Dependency Injection

---

# 1.1 Introduction

As software systems grow, classes need to collaborate with many other classes.

For example, an ML prediction service may require:

- A trained model
- A logger
- A database connection
- A configuration manager
- A metrics collector

A fundamental design question arises:

> **Who should create these objects?**

There are two possible answers:

1. The class creates its own dependencies.
2. The dependencies are provided from the outside.

Modern software engineering strongly recommends the second approach.

This principle is known as **Dependency Injection (DI).**

---

# 1.2 What Is a Dependency?

A dependency is any object that another object needs in order to perform its work.

Example:

```
PredictionPipeline
        |
        ↓
Model
```

The model is a dependency of the pipeline.

Another example:

```
TrainingService
        |
        ↓
Database
```

The database is a dependency.

---

# 1.3 Bad Design

Consider the following design:

```python
class PredictionPipeline:
    def __init__(self):

        self.model = XGBoostModel()
```

The pipeline creates the model itself.

Architecture:

```
PredictionPipeline

creates

XGBoostModel
```

This causes several problems.

---

# 1.4 Problems of Creating Dependencies Internally

## Tight Coupling

The pipeline becomes permanently connected to one implementation.

```
PredictionPipeline
        ↓
XGBoostModel
```

Replacing the model requires modifying the pipeline.

---

## Difficult Testing

Suppose we want to test only the pipeline.

The pipeline automatically creates the real model.

Testing becomes more complicated.

---

## Violates Open/Closed Principle

Adding a different model requires modifying existing code.

---

## Violates Dependency Inversion Principle

High-level components depend directly on low-level implementations.

---

# 1.5 Dependency Injection

Instead of creating dependencies internally, receive them from outside.

Example:

```python
class PredictionPipeline:
    def __init__(self, model):

        self.model = model
```

Now the pipeline no longer decides which model to use.

Someone else provides it.

Architecture:

```
main()

creates

XGBoostModel

↓

injects

↓

PredictionPipeline
```

---

# 1.6 Why "Injection"?

The word "injection" simply means:

```
Provide an object from the outside.
```

Nothing magical happens.

Instead of:

```
Pipeline

creates

Model
```

we have:

```
Someone else

creates

Model

↓

passes it

↓

Pipeline
```

The dependency is injected.

---

# 1.7 Constructor Injection

The most common form of dependency injection is constructor injection.

Example:

```python
pipeline = PredictionPipeline(model)
```

Python automatically calls:

```python
__init__(self, model)
```

The pipeline receives everything it needs during construction.

Advantages:

- Object is fully initialized.
- Dependencies cannot be forgotten.
- Simple to understand.
- Easy to test.

This is the preferred approach in most cases.

---

# 1.8 Other Types of Dependency Injection

Although constructor injection is preferred, there are other approaches.

## Setter Injection

Dependencies are assigned after construction.

Example:

```
Pipeline

↓

set_model(...)
```

Useful when dependencies are optional.

---

## Method Injection

Dependencies are passed only to a specific method.

Example:

```
pipeline.run(model)
```

Useful when the dependency is needed only temporarily.

---

# 1.9 Real Enterprise Example

Imagine a prediction service.

Without dependency injection:

```
PredictionService

creates

Logger

creates

Database

creates

Model

creates

Configuration
```

One class is responsible for everything.

With dependency injection:

```
Logger
Database
Model
Configuration

↓

PredictionService
```

Each component receives only what it needs.

Responsibilities remain separated.

---

# 1.10 Dependency Injection and Interfaces

Dependency Injection becomes even more powerful when combined with interfaces.

Instead of injecting:

```
XGBoostModel
```

inject:

```
ModelInterface
```

The pipeline now depends on an abstraction.

This allows many implementations.

```
ModelInterface

↓

XGBoostModel

RandomForestModel

LLMModel

RemoteInferenceModel
```

The pipeline remains unchanged.

---

# 1.11 Dependency Injection and Testing

Suppose we want to test the pipeline.

Production:

```
PredictionPipeline
        ↓
RealModel
```

Testing:

```
PredictionPipeline
        ↓
FakeModel
```

The pipeline behaves exactly the same.

Only the implementation changes.

This makes unit testing simple.

---

# 1.12 Dependency Injection in ML Systems

Modern ML systems commonly inject:

- Feature Store
- Model
- Logger
- Database
- Metrics Collector
- Configuration
- Cloud Client
- Message Queue
- Vector Database

None of these components should normally be created inside business logic.

---

# 1.13 Dependency Injection in FastAPI

FastAPI uses Dependency Injection extensively.

Example:

```
Endpoint

↓

Database Session

↓

Authentication

↓

Configuration
```

FastAPI automatically provides these dependencies.

Although the mechanism is more sophisticated, the underlying principle is identical:

> Objects receive what they need instead of creating it themselves.

---

# 1.14 Benefits

Dependency Injection provides several advantages.

## Lower Coupling

Components depend less on concrete implementations.

---

## Better Testability

Dependencies can easily be replaced with mocks or fake implementations.

---

## Better Maintainability

Changing one implementation rarely affects the rest of the system.

---

## Better Flexibility

New implementations can be introduced without modifying existing code.

---

## Better Scalability

Large systems become easier to extend.

---

# 1.15 Dependency Injection vs Composition

These concepts are closely related.

Composition answers:

```
Who collaborates?
```

Dependency Injection answers:

```
Who provides the collaborators?
```

Composition creates relationships.

Dependency Injection manages those relationships.

Together they produce flexible architectures.

---

# 1.16 Common Beginner Mistake

Many beginners write:

```python
class Service:
    def __init__(self):

        self.database = Database()

        self.logger = Logger()

        self.model = XGBoostModel()
```

Everything is hardcoded.

A better design is:

```python
class Service:
    def __init__(self, database, logger, model):

        self.database = database

        self.logger = logger

        self.model = model
```

Now the service is independent from specific implementations.

---

# Key Lessons

```
1. A dependency is any object another object needs.

2. Classes should not usually create their own dependencies.

3. Dependencies should be provided from outside.

4. Constructor Injection is the preferred approach.

5. Dependency Injection reduces coupling.

6. Dependency Injection simplifies testing.

7. Dependency Injection works especially well with interfaces.

8. Modern software frameworks rely heavily on Dependency Injection.
```

---

# Final Principle

> Professional software engineering separates object creation from object usage by providing dependencies from outside instead of constructing them internally.

---

# Additional Notes

## Dependency Injection does **not** create objects.

Dependency Injection is **not responsible** for creating dependencies.

Its purpose is to **provide existing dependencies** to another class.

Example:

```python
model = XGBoostModel()

service = PredictionService(model)
```

The dependency (`model`) is created outside the service and injected through the constructor.

---

## The class should not choose its dependencies.

A class should focus on **using** its collaborators, not selecting which implementation to instantiate.

Bad:

```python
self.model = XGBoostModel()
```

Good:

```python
self.model = model
```

The decision about which implementation to use belongs to a higher-level component such as `main()` or an application framework.

---

## Constructor Injection is the preferred technique.

Constructor Injection guarantees that every required dependency exists when the object is created.

Example:

```python
service = PredictionService(
    model=model,
    logger=logger,
    database=database,
)
```

The object is fully initialized before it is used.

---

## Dependency Injection works best together with Interfaces.

The injected dependency should normally be an abstraction instead of a concrete implementation.

Example:

```python
class PredictionService:
    def __init__(self, model: ModelInterface):
        self.model = model
```

The service depends on the interface rather than a specific model.

---

## Dependency Injection separates object creation from object usage.

Object creation:

```python
model = XGBoostModel()
```

Object usage:

```python
prediction = service.predict(features)
```

Separating these responsibilities produces a cleaner and more maintainable architecture.

---

## Composition + Interfaces + Dependency Injection

These three concepts work together.

Composition answers:

```
Who collaborates?
```

Interfaces answer:

```
How do they communicate?
```

Dependency Injection answers:

```
Who provides the collaborators?
```

Together they create flexible, loosely coupled software systems.

---

## Dependency Injection improves software quality.

Benefits include:

- Lower coupling.
- Easier unit testing.
- Better extensibility.
- Easier maintenance.
- Better compliance with SOLID principles.

---

## Modern software frameworks rely heavily on Dependency Injection.

Examples include:

- FastAPI
- Spring Boot
- ASP.NET Core
- NestJS

Learning the principle is more important than learning any particular framework because the underlying design philosophy remains the same.

---

## Key Lesson

Dependency Injection is not simply a programming technique.

It is an architectural pattern that separates **object creation** from **object behavior**, allowing systems to become more modular, testable, extensible, and easier to maintain.
