# 5. SOLID Principles

## Overview

SOLID is a set of five object-oriented design principles introduced by Robert C. Martin ("Uncle Bob") to help developers create software that is easier to understand, maintain, extend, and test.

These principles reduce coupling, improve cohesion, and make systems more flexible as they grow.

SOLID is one of the foundations of modern software engineering and is widely used in enterprise applications, machine learning systems, APIs, cloud architectures, and AI platforms.

---

# Single Responsibility Principle (SRP)

## Definition

> A class should have one, and only one, reason to change.

A class should focus on a single responsibility or concern.

If a class performs multiple unrelated tasks, it becomes difficult to maintain and modify.

## Benefits

- Easier maintenance
- Easier testing
- Higher cohesion
- Lower complexity
- Better readability

---

# Open/Closed Principle (OCP)

## Definition

> Software entities should be open for extension but closed for modification.

New functionality should be added by extending existing code rather than modifying code that already works.

This minimizes the risk of introducing bugs into stable components.

## Benefits

- Easier extensibility
- Reduced regression bugs
- Better maintainability
- More scalable architectures

---

# Liskov Substitution Principle (LSP)

## Definition

> Objects of a child class should be replaceable by objects of the parent class without changing the correctness of the program.

A derived class must preserve the behavior expected from its parent.

Inheritance should model a true "is-a" relationship.

## Benefits

- Reliable inheritance
- Predictable behavior
- Safer polymorphism
- Better software consistency

---

# Interface Segregation Principle (ISP)

## Definition

> Clients should not be forced to depend on methods they do not use.

Instead of creating large interfaces containing many unrelated methods, create smaller, more focused interfaces.

Classes should implement only the behaviors they actually need.

## Benefits

- Smaller interfaces
- Lower coupling
- Better flexibility
- Easier maintenance

---

# Dependency Inversion Principle (DIP)

## Definition

> High-level modules should not depend on low-level modules.
> Both should depend on abstractions.

Concrete implementations should be replaceable without affecting the higher-level logic.

Dependencies should be injected instead of being created internally.

## Benefits

- Loose coupling
- Better testability
- Easier replacement of implementations
- Greater flexibility
- Improved scalability

---

# Summary

| Principle | Main Idea |
|-----------|-----------|
| **SRP** | One class, one responsibility. |
| **OCP** | Extend behavior without modifying existing code. |
| **LSP** | Child classes must behave like their parent. |
| **ISP** | Prefer several small interfaces over one large interface. |
| **DIP** | Depend on abstractions, not concrete implementations. |

---

# Engineering Notes

- SOLID principles improve software quality as systems grow.
- They are complementary and are often applied together.
- Following SOLID generally leads to code that is easier to maintain, test, reuse, and extend.
- SOLID is widely used in enterprise software, cloud applications, APIs, AI systems, and machine learning platforms.
- Understanding SOLID is an important step toward writing production-quality software.

# Single Responsibility Principle (SRP)

## Objective

Understand why each class should have a single responsibility and a single reason to change.

## Definition

> A class should have one, and only one, reason to change.

A class should focus on a single responsibility or concern. When a class performs multiple unrelated tasks, it becomes harder to understand, maintain, test, and extend.

---

## Key Concepts

- A responsibility is a specific job or concern assigned to a class.
- A class should perform one well-defined task.
- Each class should have only one reason to change.
- Changes in one responsibility should not affect unrelated responsibilities.
- High cohesion is achieved when a class focuses on a single responsibility.

---

## Example

### Bad Design

```
MLPipeline
├── load_data()
├── preprocess_data()
├── train_model()
├── evaluate_model()
└── save_model()
```

This class performs multiple unrelated responsibilities.

Possible reasons to change:

- Data source changes
- Preprocessing changes
- Training algorithm changes
- Evaluation metric changes
- Storage location changes

Because the class has multiple reasons to change, it violates SRP.

---

### Good Design

```
DataLoader
    └── load_data()

Preprocessor
    └── preprocess_data()

ModelTrainer
    └── train_model()

ModelEvaluator
    └── evaluate_model()

ModelRepository
    └── save_model()
```

Each class has one responsibility and one reason to change.

---

## Benefits

- Easier maintenance
- Easier testing
- Better readability
- Higher cohesion
- Lower coupling
- Better scalability
- Simpler debugging

---

## Engineering Notes

- SRP does **not** mean "one method per class."
- SRP means one responsibility per class.
- A class may contain several methods if they all support the same responsibility.
- Small, focused classes are easier to reuse and extend.
- SRP is one of the foundations of clean architecture and enterprise software design.

---

## Summary

**Bad Design**

One class performs many unrelated jobs.

```
One Class
├── Job A
├── Job B
├── Job C
├── Job D
└── Job E
```

**Good Design**

Each class performs one job.

```
Class A → Job A

Class B → Job B

Class C → Job C

Class D → Job D

Class E → Job E
```

A class should change only when its own responsibility changes.