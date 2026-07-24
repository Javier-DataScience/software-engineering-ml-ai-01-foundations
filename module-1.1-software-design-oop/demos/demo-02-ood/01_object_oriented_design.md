# Engineering Exercise — Object-Oriented Design (OOD)

## Problem Statement

Design a simple Library Management System by identifying the main objects before writing any code.

## Solution

### Main Objects

| Object | Responsibility |
|---------|----------------|
| Book | Store information about a book. |
| Member | Represent a library user who can borrow books. |
| Librarian | Manage book lending and returns. |
| Loan | Record the borrowing of a book by a member. |

### Object Interactions

- A Member requests to borrow a Book.
- The Librarian processes the request.
- A Loan is created to record the transaction.
- The Book status changes to borrowed.
- When returned, the Loan is closed and the Book becomes available again.

## Discussion

Object-Oriented Design begins by identifying the important concepts in the problem domain and assigning clear responsibilities to each one. This approach produces software that is easier to understand, maintain, test, and extend than a single script containing all the logic.

## Key Takeaway

Design first, implementation second. Good software starts by identifying objects and responsibilities before writing classes and code.