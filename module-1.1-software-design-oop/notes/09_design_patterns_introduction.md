# 1. Design Patterns Introduction

---

# 1.1 Introduction

As software systems grow in size and complexity, engineers repeatedly encounter similar design problems.

Over time, experienced software engineers discovered that many of these problems could be solved using recurring architectural solutions.

These reusable solutions are called **Design Patterns**.

A design pattern is **not** a programming language feature.

A design pattern is **not** a framework.

A design pattern is a proven solution to a common software design problem.

---

# 1.2 What is a Design Pattern?

A design pattern is a general solution that describes:

- how objects collaborate,
- how responsibilities are distributed,
- how dependencies are managed,
- how software remains flexible and maintainable.

Instead of reinventing the solution every time, engineers reuse patterns that have already been validated over decades.

---

# 1.3 Design Patterns Are Templates

Design patterns should not be copied literally.

Instead, they should be viewed as architectural templates.

Each project adapts the pattern according to its own requirements.

A design pattern describes the structure of the solution rather than the exact implementation.

---

# 1.4 Why Design Patterns Exist

Without design patterns, software often becomes:

- difficult to maintain,
- difficult to extend,
- tightly coupled,
- fragile,
- repetitive.

Design patterns provide standardized approaches for solving these problems.

---

# 1.5 Design Patterns Build on Previous Principles

Design patterns are not isolated concepts.

They are built on the software engineering principles already studied:

- Object-Oriented Programming
- SOLID Principles
- Clean Code
- High Cohesion
- Low Coupling
- Composition
- Interfaces
- Dependency Injection
- Refactoring

Understanding these foundations makes design patterns much easier to learn.

---

# 1.6 Benefits of Design Patterns

Properly applied design patterns provide:

- higher flexibility,
- lower coupling,
- improved readability,
- easier maintenance,
- easier testing,
- better scalability,
- reusable architectures.

They encourage engineers to think about software architecture instead of isolated functions.

---

# 1.7 Common Categories of Design Patterns

The classic *Gang of Four* book groups design patterns into three categories.

## Creational Patterns

Focus on object creation.

Examples:

- Factory Method
- Abstract Factory
- Builder
- Prototype
- Singleton

---

## Structural Patterns

Focus on relationships between classes and objects.

Examples:

- Adapter
- Bridge
- Composite
- Decorator
- Facade
- Proxy

---

## Behavioral Patterns

Focus on communication and collaboration between objects.

Examples:

- Strategy
- Observer
- Command
- State
- Template Method
- Chain of Responsibility

---

# 1.8 Design Patterns Are Not Rules

Design patterns are recommendations.

Using a pattern when it is unnecessary introduces unnecessary complexity.

Good software engineers do not ask:

> "Which pattern can I use?"

Instead they ask:

> "Do I actually have a design problem that requires a pattern?"

Patterns should solve problems, not create them.

---

# 1.9 Overusing Design Patterns

A common mistake among beginners is forcing design patterns into every project.

This often produces:

- unnecessary abstractions,
- excessive classes,
- complicated architectures,
- reduced readability.

This phenomenon is sometimes called **overengineering**.

Simple problems usually require simple solutions.

---

# 1.10 Design Patterns in Machine Learning Systems

Modern ML and AI systems frequently use design patterns.

Examples include:

- Strategy Pattern for selecting different ML algorithms.
- Factory Pattern for creating models dynamically.
- Observer Pattern for monitoring training events.
- Builder Pattern for constructing ML pipelines.
- Facade Pattern for simplifying complex AI workflows.

Design patterns help organize large production systems while keeping components independent and maintainable.

---

# 1.11 Key Ideas

A design pattern is:

- a reusable software design solution,
- based on experience,
- independent of programming language,
- intended to improve software architecture.

Design patterns should be applied only when they simplify the design.

---

# Final Principle

> Design patterns are reusable solutions to recurring software design problems. They complement software engineering principles and help engineers build flexible, maintainable, and scalable systems without reinventing common architectural solutions.

---

# Practical Example: Strategy Pattern

## Overview

The Strategy Pattern is a behavioral design pattern that allows different behaviors to be exchanged without modifying the class that uses them.

In this exercise, we applied the pattern to an ML prediction pipeline.

The objective was to replace a design where the pipeline directly depended on specific models with a flexible architecture based on abstractions.

---

# Problem Identified in the Bad Design

The initial design used conditional logic:

```python
if model_type == "xgboost":
    model = XGBoostModel()

elif model_type == "lightgbm":
    model = LightGBMModel()
```

Problems:

- The pipeline knew all concrete models.
- The pipeline was responsible for creating model objects.
- Adding new models required modifying existing code.
- The system became harder to maintain as the number of models increased.

This created tight coupling.

---

# Improved Design With Strategy Pattern

The improved design introduced a common interface:

```python
class ModelStrategy(ABC):

    def predict(self, features):
        pass
```

Different models implemented this contract:

```
              ModelStrategy

                    |
        --------------------------
        |            |            |

    XGBoost     LightGBM    NeuralNetwork
```

The pipeline depended only on the abstraction.

---

# Important Design Concepts Applied

## Interface

The interface defines the expected behavior:

```python
predict()
```

The pipeline does not need to know how each model works.

It only knows:

> "I have an object capable of making predictions."

---

## Composition

The relationship is:

```
PredictionPipeline

        has a

ModelStrategy
```

The pipeline uses a strategy object instead of inheriting from a model.

---

## Dependency Injection

The strategy is provided externally:

```python
model_strategy = XGBoostStrategy()

pipeline = PredictionPipeline(model_strategy)
```

The pipeline receives the collaborator instead of creating it internally.

Benefits:

- Lower coupling.
- Easier testing.
- Easier replacement of implementations.

---

## Open/Closed Principle

A new model can be added:

```python
class RandomForestStrategy(ModelStrategy):
```

without modifying:

```python
PredictionPipeline
```

The system is open for extension and closed for modification.

---

# Main Engineering Lesson

The Strategy Pattern changes the design question.

Instead of asking:

> "Which implementation should this class create?"

we ask:

> "What behavior does this class need, and who can provide it?"

This allows ML systems to change models, algorithms, or behaviors without rewriting existing components.

---

# ML Engineering Connection

This pattern is highly relevant in ML/AI systems:

Examples:

- Switching ML models.
- Changing inference engines.
- Selecting preprocessing strategies.
- Changing retrieval strategies in RAG systems.
- Switching LLM providers.

The architecture remains stable while implementations evolve.