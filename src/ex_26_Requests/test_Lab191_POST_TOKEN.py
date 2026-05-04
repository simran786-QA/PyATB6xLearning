# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: API Testing – Create Auth Token (POST /auth)
# -------------------------------------------------------------

import pytest
import allure
import requests


# -------------------------------------------------------------
# Test Case: Create Auth Token
# -------------------------------------------------------------
@allure.title("TC#1 - Create Auth Token")
@allure.description("Verify that auth token is generated successfully")
@pytest.mark.auth
def test_create_token():

    # ---------------------------------------------------------
    # Step 1: URL
    # ---------------------------------------------------------
    base_url = "https://restful-booker.herokuapp.com"
    full_url = base_url + "/auth"

    # ---------------------------------------------------------
    # Step 2: Headers
    # ---------------------------------------------------------
    headers = {"Content-Type": "application/json"}

    # ---------------------------------------------------------
    # Step 3: Payload
    # ---------------------------------------------------------
    payload = {
        "username": "admin",
        "password": "password123"
    }

    # ---------------------------------------------------------
    # Step 4: Send POST request
    # ---------------------------------------------------------
    response = requests.post(url=full_url, headers=headers, json=payload)

    # Debug (better than printing object)
    print(response.text)

    # ---------------------------------------------------------
    # Step 5: Validate status code
    # ---------------------------------------------------------
    assert response.status_code == 200

    # ---------------------------------------------------------
    # Step 6: Validate response JSON
    # ---------------------------------------------------------
    response_json = response.json()

    assert "token" in response_json

    token = response_json["token"]

    # ---------------------------------------------------------
    # Step 7: Validate token
    # ---------------------------------------------------------
    assert isinstance(token, str)
    assert len(token) > 0