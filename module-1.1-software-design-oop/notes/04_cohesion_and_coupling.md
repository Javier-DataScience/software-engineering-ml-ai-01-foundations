# 1. Cohesion and Coupling

---

## 1.1 Introduction

Cohesion and Coupling are two of the most important concepts in software engineering.

They help engineers evaluate the quality of a software design independently of the programming language.

A well-designed system generally has:

- High Cohesion.
- Low Coupling.

These two concepts complement each other.

A highly cohesive system with low coupling is easier to:

- Understand.
- Maintain.
- Test.
- Extend.
- Reuse.

---

# 1.2 Cohesion

Cohesion describes how closely related the responsibilities of a module, class, or function are.

A component has **high cohesion** when everything inside it contributes to a single, well-defined purpose.

Example:

```
ModelTrainer

↓

Receive training data

↓

Train the model

↓

Return the trained model
```

Everything inside the component contributes to the same objective.

---

## High Cohesion

A highly cohesive component:

- Has one clear responsibility.
- Has one reason to change.
- Is easier to understand.
- Is easier to test.
- Is easier to reuse.

Example:

```
DataLoader

↓

Load data only
```

Another example:

```
ModelEvaluator

↓

Evaluate model performance only
```

---

## Low Cohesion

Low cohesion occurs when unrelated responsibilities are grouped together.

Example:

```
MLSystem

↓

Load data

↓

Train model

↓

Deploy API

↓

Send email

↓

Generate reports
```

Problems:

- Multiple responsibilities.
- Difficult maintenance.
- Difficult testing.
- Violates the Single Responsibility Principle.

---

# 1.3 Coupling

Coupling describes the level of dependency between components.

The more one component depends on another, the higher the coupling.

---

## High Coupling

Example:

```
TrainingService

↓

RandomForestModel
```

The service depends directly on one specific implementation.

Problems:

- Difficult replacement.
- Difficult testing.
- Difficult extension.

Changing the model may require modifying multiple classes.

---

## Low Coupling

Example:

```
TrainingService

↓

MLModel (Interface)

↓

RandomForestModel

XGBoostModel

NeuralNetworkModel
```

The service depends on an abstraction rather than a concrete implementation.

Benefits:

- Flexible.
- Testable.
- Easier to extend.

---

# 1.4 Relationship Between Cohesion and Coupling

Good software design seeks:

```
High Cohesion

+

Low Coupling
```

These concepts reinforce each other.

When responsibilities are clearly separated:

- Components become more cohesive.
- Dependencies naturally decrease.

---

## Example

Poor design:

```
Pipeline

↓

Load data

↓

Train model

↓

Deploy API

↓

Monitor system
```

Problems:

- Low cohesion.
- High coupling.
- Multiple responsibilities.

Better design:

```
DataLoader

↓

Preprocessor

↓

ModelTrainer

↓

ModelEvaluator

↓

ModelRegistry

↓

DeploymentService

↓

MonitoringService
```

Each component has:

- High cohesion.
- Lower coupling.

---

# 1.5 Cohesion and SOLID

Many SOLID principles help improve cohesion and reduce coupling.

Examples:

## Single Responsibility Principle

Improves cohesion.

Each class focuses on one responsibility.

---

## Dependency Inversion Principle

Reduces coupling.

Components depend on abstractions instead of concrete implementations.

---

## Interface Segregation Principle

Reduces unnecessary dependencies.

Clients only depend on the interfaces they actually use.

---

# 1.6 Cohesion and Clean Code

Clean Code naturally promotes:

- High cohesion.
- Low coupling.

Example:

Bad:

```
training_pipeline.py

↓

Load data

↓

Train model

↓

Deploy model

↓

Send notification
```

Better:

```
data_loader.py

model_trainer.py

deployment_service.py

notification_service.py
```

Each module has a single purpose.

---

# 1.7 Cohesion and ML/AI Systems

Machine Learning systems evolve continuously.

Examples:

- New datasets.
- New preprocessing steps.
- New models.
- New evaluation metrics.
- New deployment strategies.

If responsibilities are separated:

```
Data

↓

Training

↓

Evaluation

↓

Deployment

↓

Monitoring
```

each component can evolve independently.

This makes production ML systems:

- More maintainable.
- More scalable.
- Easier to test.

---

# 1.8 Cohesion and Enterprise AI Platforms

Enterprise AI platforms are composed of many independent services.

Typical architecture:

```
Data Ingestion

↓

Feature Engineering

↓

Model Training

↓

Model Registry

↓

Inference API

↓

Monitoring

↓

Retraining Pipeline
```

Each service performs one specialized responsibility.

Services communicate through clearly defined interfaces.

This architecture maximizes:

- High cohesion.
- Low coupling.

---

# 1.9 Main Lesson

Professional software design aims to build systems with:

- High cohesion.
- Low coupling.

These principles improve:

- Maintainability.
- Flexibility.
- Testability.
- Scalability.

Many software engineering practices—including SOLID, Clean Code, Refactoring, and Design Patterns—are ultimately techniques for increasing cohesion and reducing coupling.

---
# 2. Cohesion and Coupling Summary

---

## 2.1 Cohesion

Cohesion measures how closely related the responsibilities inside a module, class, or function are.

A component has **high cohesion** when everything inside it contributes to one clear objective.

Example:

```
ModelTrainer

↓

Receive training data

↓

Train model

↓

Return trained model
```

All responsibilities support the same purpose.

---

## 2.2 High Cohesion

Characteristics:

- One well-defined responsibility.
- One reason to change.
- Easier to understand.
- Easier to test.
- Easier to maintain.
- Easier to reuse.

Example:

```
DataLoader

↓

Load data only
```

or

```
ModelEvaluator

↓

Evaluate model performance only
```

---

## 2.3 Low Cohesion

Low cohesion occurs when unrelated responsibilities are grouped together.

Example:

```
MLSystem

↓

Load data

↓

Train model

↓

Deploy API

↓

Monitor system

↓

Send notifications
```

Problems:

- Multiple responsibilities.
- Difficult maintenance.
- Difficult testing.
- Difficult extension.
- Usually violates the Single Responsibility Principle.

---

## 2.4 Coupling

Coupling measures how dependent one component is on another.

The stronger the dependency between components, the higher the coupling.

---

## 2.5 High Coupling

Example:

```
TrainingService

↓

RandomForestModel
```

Problems:

- Difficult to replace implementations.
- Difficult to test.
- Difficult to extend.
- Changes propagate across the system.

---

## 2.6 Low Coupling

Example:

```
TrainingService

↓

MLModel Interface

↓

RandomForestModel

XGBoostModel

NeuralNetworkModel
```

Benefits:

- Flexible design.
- Easier testing.
- Easier replacement of implementations.
- Better scalability.

Low coupling is one of the primary objectives of software architecture.

---

## 2.7 Relationship Between Cohesion and Coupling

Professional software systems aim for:

```
High Cohesion

+

Low Coupling
```

High cohesion focuses on the responsibilities **inside** a component.

Low coupling focuses on the dependencies **between** components.

Although related, they measure different characteristics of software design.

---

## 2.8 Relationship with SOLID

Several SOLID principles improve cohesion and reduce coupling.

Examples:

### Single Responsibility Principle

Improves cohesion by ensuring each class has one responsibility.

---

### Dependency Inversion Principle

Reduces coupling by depending on abstractions rather than concrete implementations.

---

### Interface Segregation Principle

Reduces unnecessary dependencies by exposing only the operations clients require.

---

## 2.9 Relationship with Clean Code

Clean Code naturally promotes:

- High cohesion.
- Low coupling.

Example:

Poor design:

```
training_pipeline.py

↓

Load data

↓

Train model

↓

Deploy model

↓

Send notification
```

Better design:

```
data_loader.py

model_trainer.py

deployment_service.py

notification_service.py
```

Each module has one focused responsibility.

---

## 2.10 Cohesion and Coupling in ML Systems

Production ML systems continuously evolve.

Typical changes include:

- New datasets.
- New preprocessing pipelines.
- New models.
- New evaluation metrics.
- New deployment strategies.

Separating responsibilities allows these components to evolve independently.

Example architecture:

```
Data

↓

Training

↓

Evaluation

↓

Deployment

↓

Monitoring
```

This improves maintainability and scalability.

---

## 2.11 Enterprise AI Systems

Enterprise AI platforms are composed of multiple specialized services.

Example:

```
Data Ingestion

↓

Feature Engineering

↓

Model Training

↓

Model Registry

↓

Inference API

↓

Monitoring

↓

Retraining Pipeline
```

Each service focuses on one responsibility while communicating through clearly defined interfaces.

This architecture promotes:

- High cohesion.
- Low coupling.
- Independent evolution of components.

---

## 2.12 Mental Model

When reviewing software, ask two questions:

### Cohesion

```
Do all responsibilities inside this component belong together?
```

### Coupling

```
How dependent is this component on other components?
```

These two questions quickly reveal many architectural problems.

---

## 2.13 Main Lesson

Good software engineering seeks to maximize cohesion while minimizing coupling.

Many engineering practices—including:

- SOLID,
- Clean Code,
- Refactoring,
- Design Patterns,

are ultimately techniques for increasing cohesion and reducing coupling.

These principles produce systems that are easier to understand, maintain, test, and evolve over time.

---

# 3. Demo 15 Review — Cohesion and Coupling

---

## 3.1 Objective

The objective of this demo was to demonstrate the relationship between:

- Cohesion
- Coupling

using a simple Machine Learning system.

Both implementations produce the same output.

The difference is entirely architectural.

---

# 3.2 Bad Design Analysis

The bad implementation concentrated multiple responsibilities inside a single class.

```
MLSystem

↓

Load data

↓

Generate predictions

↓

Evaluate model

↓

Deploy model

↓

Send notification
```

Problems:

- Low cohesion.
- High coupling.
- Difficult maintenance.
- Difficult testing.
- Difficult extension.

---

## Low Cohesion

The class performs unrelated tasks.

Responsibilities include:

- Data loading.
- Prediction.
- Evaluation.
- Deployment.
- Notification.

The class has multiple reasons to change.

---

## High Coupling

The class directly creates:

```
RandomForestModel()
```

This means the class depends on one concrete implementation.

Changing the model requires modifying the class itself.

---

# 3.3 Good Design Analysis

The responsibilities were separated into specialized components.

```
DataLoader

↓

ModelTrainer

↓

ModelEvaluator

↓

DeploymentService

↓

NotificationService
```

Each component performs one specific responsibility.

---

## High Cohesion

Each class focuses on one objective.

Examples:

```
DataLoader

↓

Load data
```

```
DeploymentService

↓

Deploy model
```

```
NotificationService

↓

Notify completion
```

Each component has one reason to change.

---

## Low Coupling

ModelTrainer depends on an abstraction.

```
ModelTrainer

↓

MLModel Interface

↓

RandomForestModel
```

The trainer does not know which concrete model it receives.

This makes the system easier to extend.

---

# 3.4 Engineering Benefits

The refactored version provides several advantages.

## Easier Testing

Each class can be tested independently.

Example:

```
Test DataLoader

Test ModelEvaluator

Test DeploymentService
```

---

## Easier Maintenance

Changes remain isolated.

Changing the deployment process does not affect:

- Data loading.
- Training.
- Evaluation.

---

## Easier Extension

A new model can be added without modifying ModelTrainer.

Example:

```
MLModel

↓

RandomForestModel

XGBoostModel

LightGBMModel

NeuralNetworkModel
```

The trainer continues working without modification.

---

# 3.5 Concepts Reinforced

This demo connects several software engineering concepts.

## Single Responsibility Principle

Each class performs one responsibility.

---

## Dependency Inversion Principle

The trainer depends on an abstraction instead of a concrete implementation.

---

## Clean Code

Small focused components improve readability.

---

## Code Smells

The bad implementation demonstrated:

- Low cohesion.
- High coupling.
- Large class.

---

## Cohesion and Coupling

Professional software design seeks:

```
High Cohesion

+

Low Coupling
```

This combination produces systems that are easier to understand, maintain, test, and extend.

---

# 3.6 Main Lesson

Good software architecture is not about making systems more complex.

It is about organizing responsibilities so that each component has a clear purpose while minimizing unnecessary dependencies between components.

Professional engineers continuously refactor software to increase cohesion and reduce coupling as systems evolve.

---