# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: PyTest – Custom Marker, Regression & Skip
# -------------------------------------------------------------

import pytest
import allure
import requests  # (not used here, can be removed)


# -------------------------------------------------------------
# Test Case 1: Basic Math (Custom Marker - tapas)
# -------------------------------------------------------------
@allure.title("TC#1 - Verify that 2-2 == 0")
@allure.description("This is a BASIC Math Test")
@pytest.mark.tapas
def test_basic_math():

    # Step 1: Assertion (pass)
    assert 2 - 2 == 0


# -------------------------------------------------------------
# Test Case 2: Regression Test (Pass)
# -------------------------------------------------------------
@allure.title("TC#2 - Verify that 3-3 is equal to 0")
@allure.description("This is a smoke Testcase which checks 3-3 == 0")
@pytest.mark.regression
def test_sub1():

    # Step 1: Assertion (pass)
    assert 3 - 3 == 0


# -------------------------------------------------------------
# Test Case 3: Skipped Test
# -------------------------------------------------------------
@pytest.mark.skip(reason="Not working, Skip it")
def test_sub3():

    # This will be skipped (not executed)
    assert 0 - 0 != 0