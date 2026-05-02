# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: API Testing – POST (Create Booking) Positive & Negative
# -------------------------------------------------------------

import pytest
import allure
import requests


# -------------------------------------------------------------
# Test Case 1: Create Booking (Positive)
# -------------------------------------------------------------
@allure.title("TC#1 - Create Booking CRUD Positive")
@allure.description("Verify the create booking API with valid payload")
@pytest.mark.crud
def test_create_booking_positive_tc1():

    # Step 1: URL
    base_url = "https://restful-booker.herokuapp.com"
    full_url = base_url + "/booking"

    # Step 2: Headers
    headers = {"Content-Type": "application/json"}

    # Step 3: Payload
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    # Step 4: API call
    response = requests.post(url=full_url, headers=headers, json=payload)

    # Step 5: Status validation
    assert response.status_code == 200

    # Step 6: JSON parsing
    response_json = response.json()

    # Step 7: Validate booking id
    booking_id = response_json["bookingid"]
    assert booking_id is not None
    assert booking_id > 0
    assert isinstance(booking_id, int)

    # Step 8: Validate response data
    booking = response_json["booking"]

    assert booking["firstname"] == "Jim"
    assert booking["lastname"] == "Brown"
    assert booking["totalprice"] == 111
    assert booking["depositpaid"] is True

    # Step 9: Nested validation
    assert booking["bookingdates"]["checkin"] == "2018-01-01"
    assert booking["bookingdates"]["checkout"] == "2019-01-01"

    # Step 10: Response time validation
    assert response.elapsed.total_seconds() < 3


# -------------------------------------------------------------
# Test Case 2: Create Booking (Negative)
# -------------------------------------------------------------
@allure.title("TC#2 - Create Booking CRUD Negative")
@allure.description("Verify that invalid payload does not create booking")
@pytest.mark.crud
def test_create_booking_negative_tc1():

    # Step 1: URL
    url = "https://restful-booker.herokuapp.com/booking"

    # Step 2: Headers
    headers = {"Content-Type": "application/json"}

    # Step 3: Invalid payload
    payload = {}

    # Step 4: API call
    response = requests.post(url=url, headers=headers, json=payload)

    # Step 5: Validate failure
    assert response.status_code == 500