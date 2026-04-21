# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: PyTest – Markers (smoke tests) & Assertions
# -------------------------------------------------------------

import pytest


# -------------------------------------------------------------
# Test Case 1: Failing test (intentional)
# -------------------------------------------------------------
@pytest.mark.smoke
def test_method1():

    # Step 1: Print message
    print("Hello World")

    # Step 2: Assertion (will fail)
    assert 5 == 6


# -------------------------------------------------------------
# Test Case 2: Passing test
# -------------------------------------------------------------
@pytest.mark.smoke
def test_method2():

    # Step 1: Print message
    print("Hello World")

    # Step 2: Assertion (will pass)
    assert 5 == 5