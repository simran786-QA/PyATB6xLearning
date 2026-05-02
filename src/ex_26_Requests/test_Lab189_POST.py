# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: API Testing – POST (Create Booking) using requests + pytest + allure
# -------------------------------------------------------------

import pytest
import allure
import requests


# -------------------------------------------------------------
# Test Case: Create Booking (Positive)
# -------------------------------------------------------------
@allure.title("TC#1 - Create Booking CRUD Positive")
@allure.description("Verify the create booking API returns 200 and valid response body")
@pytest.mark.crud
def test_create_booking_positive_tc1():

    # ---------------------------------------------------------
    # Step 1: Define URL
    # ---------------------------------------------------------
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    full_url = base_url + base_path

    # ---------------------------------------------------------
    # Step 2: Headers
    # ---------------------------------------------------------
    headers = {
        "Content-Type": "application/json"
    }

    # ---------------------------------------------------------
    # Step 3: Payload
    # ---------------------------------------------------------
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

    # ---------------------------------------------------------
    # Step 4: Send POST request
    # ---------------------------------------------------------
    response = requests.post(url=full_url, headers=headers, json=payload)

    # Debug log
    print(response.text)

    # ---------------------------------------------------------
    # Step 5: Validate Status Code
    # ---------------------------------------------------------
    assert response.status_code == 200

    # ---------------------------------------------------------
    # Step 6: Validate Response Body (JSON)
    # ---------------------------------------------------------
    response_json = response.json()

    # bookingid should be present and > 0
    assert "bookingid" in response_json
    assert response_json["bookingid"] > 0

    # validate returned booking data
    booking = response_json["booking"]
    assert booking["firstname"] == payload["firstname"]
    assert booking["lastname"] == payload["lastname"]
    assert booking["totalprice"] == payload["totalprice"]