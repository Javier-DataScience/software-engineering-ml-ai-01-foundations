"""
PIP:
    PEP 8 – Style Guide for Python Code
    https://peps.python.org/pep-0008/

Module:
    Phase 1 – Professional Python Software Engineering Foundations
    Module 1.1 – Software Design & Object-Oriented Programming
    demo-19-refactoring
    File: bad_design.py

Purpose:
    Demonstrate a poorly designed Machine Learning prediction pipeline.
    The implementation intentionally contains several code smells that
    will be refactored in the next example without changing the
    observable behavior of the program.
"""

# =============================================================================
# Function
# =============================================================================


def run_pipeline():  # Performs the entire ML workflow inside one function.

    x = [10, 20, 30, 40]  # Poor variable name.

    a = []  # Poor variable name.

    # Duplicate normalization logic.
    for i in x:
        a.append(i / 40)  # Magic number.

    b = []  # Poor variable name.

    # Duplicate normalization logic again.
    for i in x:
        b.append(i / 40)  # Magic number.

    m = {"t": 0.8}  # Poor key name and magic number.

    p = []  # Poor variable name.

    # Generate predictions.
    for value in a:
        # Hardcoded decision threshold.
        if value > m["t"]:
            p.append(1)
        else:
            p.append(0)

    # Display predictions.
    print("Predictions:", p)


# =============================================================================
# Entry Point
# =============================================================================

if __name__ == "__main__":
    # Execute the ML workflow.
    run_pipeline()
