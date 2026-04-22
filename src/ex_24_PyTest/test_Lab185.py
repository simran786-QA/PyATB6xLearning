# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: PyTest – Multiple Markers (smoke & regression)
# -------------------------------------------------------------

import pytest


# -------------------------------------------------------------
# Test Case 1: Smoke Test (Failing)
# -------------------------------------------------------------
@pytest.mark.smoke
def test_method2():

    # Step 1: Print message
    print("test1")

    # Step 2: Assertion (will fail)
    assert 1 - 1 == 2


# -------------------------------------------------------------
# Test Case 2: Regression Test (Passing)
# -------------------------------------------------------------
@pytest.mark.regression
def test_login():

    # Step 1: Print message
    print("test2")

    # Step 2: Assertion (will pass)
    assert 1 + 1 == 2