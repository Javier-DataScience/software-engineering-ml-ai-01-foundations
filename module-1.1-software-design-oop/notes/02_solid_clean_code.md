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

# Open/Closed Principle (OCP)

## Objective

Understand how to design software that is easy to extend without modifying existing, working code.

---

## Definition

> **Software entities should be open for extension but closed for modification.**

This means:

- We should be able to add new behavior.
- We should avoid changing code that already works.

Instead of modifying existing classes, we extend the system by creating new classes.

---

## Why OCP Exists

Imagine a system that calculates discounts.

Initially it supports:

- Student
- Premium

Later the business asks for:

- VIP
- Gold
- Employee
- Partner

A poor design forces us to edit the same class every time a new discount is added.

Every modification introduces risk:

- New bugs
- Broken existing features
- Difficult testing
- Merge conflicts in team environments

OCP avoids these problems.

---

## Bad Design

```
                DiscountCalculator

                 calculate()

          if Student
             ...

          elif Premium
             ...

          elif VIP
             ...

          elif Gold
             ...

          elif Employee
             ...
```

Every new customer type requires changing the same class.

This violates OCP.

---

## Good Design

```
                DiscountStrategy
                    (abstract)

                 calculate()

          ▲         ▲        ▲
          │         │        │
     Student   Premium    VIP
     Discount  Discount  Discount
```

When a new discount is needed:

```
PartnerDiscount
```

we simply create another class.

The existing classes remain unchanged.

---

## Key Concepts

- Existing code should remain stable.
- New functionality should be added through extension.
- Avoid large `if-elif-else` chains that constantly grow.
- Prefer polymorphism over conditional logic.
- OCP works together with inheritance and abstraction.

---

## Benefits

- Easier maintenance.
- Easier testing.
- Lower risk of introducing bugs.
- Better scalability.
- Cleaner architecture.
- Easier teamwork.

---

## AI / ML Engineering Example

Imagine an LLM application.

Bad design:

```
if provider == "OpenAI":
    ...

elif provider == "Claude":
    ...

elif provider == "Gemini":
    ...

elif provider == "Llama":
    ...
```

Every new provider forces us to modify the application.

Using OCP:

```
LLMProvider
    ▲
    │
OpenAIProvider

ClaudeProvider

GeminiProvider

LlamaProvider
```

Adding a new model becomes:

```
DeepSeekProvider
```

No existing code needs to change.

---

## Engineering Notes

- OCP reduces maintenance costs.
- It encourages extensible software architecture.
- It relies heavily on abstraction and polymorphism.
- Most enterprise software frameworks follow this principle.
- OCP is one of the foundations of scalable object-oriented design.

## The Open/Closed Principle is achieved by combining abstraction, inheritance, and polymorphism.

The system depends on a stable abstraction (Notification) instead of concrete implementations (Email, SMS, Push).

New behaviors can be added by creating new classes that follow the same interface, without modifying existing code.

# Open/Closed Principle (OCP)

## Objective

Understand how to design software that can be extended with new functionality without modifying existing working code.

---

## Definition

The Open/Closed Principle (OCP) states:

> Software entities should be open for extension but closed for modification.

This means:

- A system should allow new behavior to be added.
- Existing working code should remain stable.
- New functionality should be introduced through extension.

---

## Why OCP Exists

Software systems continuously evolve.

New requirements appear:

- New features.
- New integrations.
- New business rules.
- New technologies.

A poor design requires modifying existing classes every time a new requirement appears.

This increases:

- Risk of introducing bugs.
- Testing complexity.
- Maintenance cost.
- Code coupling.

OCP helps create systems that can grow safely.

---

# Bad Design Example

A notification system implemented with conditional logic:

```
class NotificationService:

    def send_notification(self, notification_type, message):

        if notification_type == "email":
            print(f"Sending EMAIL: {message}")

        elif notification_type == "sms":
            print(f"Sending SMS: {message}")

        elif notification_type == "push":
            print(f"Sending PUSH: {message}")
```

The problem:

Every time a new notification type is added, the existing class must be modified.

Example:

Adding WhatsApp requires:

```
elif notification_type == "whatsapp":
    print(f"Sending WhatsApp: {message}")
```

The class keeps growing.

This violates OCP because the existing code is not closed for modification.

---

# Good Design Example

Using abstraction and polymorphism:

```
                 Notification
                    (ABC)

                       |
        --------------------------------
        |              |               |
      Email           SMS            Push
   Notification   Notification   Notification
```

Each notification type implements the same contract:

```
send(message)
```

The service depends only on the abstraction:

```
class NotificationService:

    def send(self, notification, message):
        notification.send(message)
```

The service does not need to know if the object is:

```
EmailNotification

SMSNotification

PushNotification
```

It only knows that the object can execute:

```
send()
```

---

# Relationship with Previous OOP Concepts

OCP is achieved by combining several Object-Oriented Programming concepts.

---

## Inheritance

Child classes inherit from a common abstraction:

```
class EmailNotification(Notification):
```

```
class SMSNotification(Notification):
```

```
class PushNotification(Notification):
```

They share the same parent contract.

---

## Abstraction

The abstract class defines what every notification must provide:

```
class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass
```

The abstraction hides implementation details.

The parent defines the required behavior, while children decide how to implement it.

---

## Polymorphism

Different objects respond to the same method differently.

The common method is:

```
notification.send(message)
```

Example:

```
email.send("Hello")
```

Output:

```
Sending EMAIL: Hello
```

Another object:

```
sms.send("Hello")
```

Output:

```
Sending SMS: Hello
```

Same method.

Different behavior.

---

# Adding New Functionality

Suppose the system needs WhatsApp notifications.

Without OCP:

```
Modify NotificationService.

Add another condition.

Risk breaking existing code.
```

With OCP:

Create a new class:

```
class WhatsAppNotification(Notification):

    def send(self, message):
        print(f"Sending WhatsApp: {message}")
```

The existing system remains unchanged.

The software is extended, not modified.

---

# AI / ML Engineering Example

Imagine an LLM application supporting different providers.

Bad design:

```
if provider == "OpenAI":
    ...

elif provider == "Claude":
    ...

elif provider == "Gemini":
    ...

elif provider == "Llama":
    ...
```

Every new provider forces us to modify the application.

Using OCP:

```
              LLMProvider
                  (ABC)

                    |
    --------------------------------
    |              |               |
OpenAIProvider  ClaudeProvider  GeminiProvider
```

Adding a new model becomes:

```
DeepSeekProvider
```

No existing code needs to change.

---

# Key Concepts

- Existing code should remain stable.
- New functionality should be added through extension.
- Avoid large `if-elif-else` chains that constantly grow.
- Prefer polymorphism over conditional logic.
- OCP works together with inheritance and abstraction.

---

# Benefits

- Easier maintenance.
- Easier testing.
- Lower risk of introducing bugs.
- Better scalability.
- Cleaner architecture.
- Easier teamwork.

---

# Engineering Notes

- OCP reduces the impact of future changes.
- Stable abstractions protect existing code.
- New behavior should be added through extension.
- OCP is one of the foundations of scalable software architecture.

OCP works together with:

```
Abstraction
Inheritance
Polymorphism
Dependency Injection
```

---

# Key Takeaway

A good software design does not try to predict every future requirement.

Instead, it creates structures where new requirements can be added safely without constantly rewriting existing code.