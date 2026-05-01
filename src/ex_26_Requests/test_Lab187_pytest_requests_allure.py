# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: API Testing – GET Request using requests + pytest + allure
# -------------------------------------------------------------

import pytest
import allure
import requests


# -------------------------------------------------------------
# Test Case 1: Valid GET Request (Positive)
# -------------------------------------------------------------
@allure.title("TC#1 - Verify the GET request.")
@allure.description("Verify that the GET request is successful and returns 200 OK.")
@pytest.mark.positive
def test_get_request():

    # Step 1: Define URL
    url = "https://restful-booker.herokuapp.com/booking/1"

    # Step 2: Send GET request
    response_data = requests.get(url=url)

    # Step 3: Validate status code
    assert response_data.status_code == 200


# -------------------------------------------------------------
# Test Case 2: Invalid ID GET Request (Negative)
# -------------------------------------------------------------
@allure.title("Verify the GET Request with invalid ID")
@allure.description("Verify booking with invalid ID returns 404")
@pytest.mark.negative
def test_get_request_negative():

    # Step 1: Define invalid URL
    url_get = "https://restful-booker.herokuapp.com/booking/-1"

    # Step 2: Send GET request
    response_data = requests.get(url=url_get)

    # Step 3: Validate status code
    assert response_data.status_code == 404