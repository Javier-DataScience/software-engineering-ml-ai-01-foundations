"""
===============================================================================
Module: bad_design.py

Path: module-1.1-software-design-oop/demos/demo-14-code-smells/bad_design.py

Purpose:
Demonstrate several common Code Smells in a simple Machine Learning pipeline.

The code executes correctly but intentionally contains poor software
engineering practices.

===============================================================================
"""


# Functions


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

    # Deep nesting begins.
    for i in a:
        if i >= 0:
            if i <= 1:
                if m:
                    if i > m["t"]:
                        p.append(1)

                    else:
                        p.append(0)

    e = [0, 0, 1, 1]  # Poor variable name.

    c = 0  # Poor variable name.

    for i in range(len(p)):  # Evaluate predictions.
        if p[i] == e[i]:
            c += 1

    acc = c / len(e)  # Poor variable name.

    print("Data:", x)

    print("Processed:", a)

    print("Model:", m)

    print("Predictions:", p)

    print("Accuracy:", acc)

    print("Saving model...")  # Mixed responsibility.

    print("Sending notification...")  # Mixed responsibility.


# Main


def main():  # Coordinates the demonstration.

    run_pipeline()  # Execute the complete pipeline.


# Entry Point

if __name__ == "__main__":  # Script entry point.
    main()  # Start the demonstration.
