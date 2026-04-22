# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: PyTest + Allure – Markers (positive/negative/regression)
# -------------------------------------------------------------

import pytest
import allure


# -------------------------------------------------------------
# Test Case 1: Positive (Failing intentionally)
# -------------------------------------------------------------
@allure.title("Verify that the create booking is working.")
@allure.description("We are going to verify the create booking in the future of this function.")
@pytest.mark.positive
@pytest.mark.regression
def test_create_booking_positive():

    # Step 1: Log
    print("test1")

    # Step 2: Assertion (will fail)
    assert 1 - 1 == 2


# -------------------------------------------------------------
# Test Case 2: Negative (Passing)
# -------------------------------------------------------------
@allure.title("Verify that create booking, with invalid data is working")
@allure.description("This Testcase checks negative create booking")
@pytest.mark.negative
def test_create_booking_negative_1():

    # Step 1: Log
    print("test2")

    # Step 2: Assertion (will pass)
    assert 1 + 1 == 2


# -------------------------------------------------------------
# Test Case 3: Negative (Passing)
# -------------------------------------------------------------
@allure.title("Verify that create booking, with invalid data is working")
@allure.description("This Testcase checks negative create booking")
@pytest.mark.negative
def test_create_booking_negative_2():

    # Step 1: Log
    print("test2")

    # Step 2: Assertion (will pass)
    assert 1 + 1 == 2