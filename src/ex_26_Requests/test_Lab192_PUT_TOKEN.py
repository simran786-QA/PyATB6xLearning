# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: API Chaining – Auth → Create → Update → Delete
# -------------------------------------------------------------

import pytest
import allure
import requests


# -------------------------------------------------------------
# Global Config
# -------------------------------------------------------------
BASE_URL = "https://restful-booker.herokuapp.com"
HEADERS = {"Content-Type": "application/json"}


# -------------------------------------------------------------
# Helper: Get Auth Token
# -------------------------------------------------------------
def get_token():
    url = BASE_URL + "/auth"

    payload = {
        "username": "admin",
        "password": "password123"
    }

    response = requests.post(url=url, headers=HEADERS, json=payload)

    assert response.status_code == 200

    response_json = response.json()
    token = response_json["token"]

    assert isinstance(token, str)
    assert len(token) > 0

    return token


# -------------------------------------------------------------
# Helper: Create Booking → return booking_id
# -------------------------------------------------------------
def get_booking_id():
    url = BASE_URL + "/booking"

    payload = {
        "firstname": "Amit",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(url=url, headers=HEADERS, json=payload)

    assert response.status_code == 200

    booking_id = response.json()["bookingid"]

    assert booking_id > 0

    return booking_id


# -------------------------------------------------------------
# Test Case: Update Booking (PUT)
# -------------------------------------------------------------
@allure.title("TC#1 - Update Booking using Token")
@pytest.mark.crud
def test_put():

    token = get_token()
    booking_id = get_booking_id()

    url = BASE_URL + "/booking/" + str(booking_id)

    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={token}"
    }

    payload = {
        "firstname": "Pramod",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(url=url, headers=headers, json=payload)

    assert response.status_code == 200
    assert response.json()["firstname"] == "Pramod"


# -------------------------------------------------------------
# Test Case: Delete Booking
# -------------------------------------------------------------
@allure.title("TC#2 - Delete Booking using Token")
@pytest.mark.crud
def test_delete():

    token = get_token()
    booking_id = get_booking_id()

    url = BASE_URL + "/booking/" + str(booking_id)

    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={token}"
    }

    response = requests.delete(url=url, headers=headers)

    assert response.status_code == 201