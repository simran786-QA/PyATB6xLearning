# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Selenium Exception Handling – NoSuchElementException
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 1: Import required Selenium modules
# -------------------------------------------------------------
# NoSuchElementException is used to handle element not found cases.
# webdriver is used to control the browser.

from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver


# -------------------------------------------------------------
# Step 2: Perform browser actions inside try block
# -------------------------------------------------------------
# Any Selenium action that may fail is placed inside try.

try:
    driver = webdriver.Chrome()
    driver.get("https://example.com")

    # Trying to locate an element that does not exist
    driver.find_element("id", "not exist button")


# -------------------------------------------------------------
# Step 3: Handle NoSuchElementException
# -------------------------------------------------------------
# This block runs when Selenium cannot find the element.

except NoSuchElementException as nse:
    print("Element not found!", nse.msg)


# -------------------------------------------------------------
# Hindi Explanation:
# - Selenium webdriver Chrome browser open karta hai.
# - example.com website load hoti hai.
# - Ek aise element ko find karne ki koshish ki ja rahi hai
#   jo page par exist nahi karta.
# - Is situation mein Selenium NoSuchElementException throw karta hai.
# - except block error ko handle karta hai aur message print karta hai.
#
# English Explanation:
# - Chrome browser is launched using Selenium WebDriver.
# - The website example.com is opened.
# - Selenium tries to locate a non-existing element.
# - NoSuchElementException is raised.
# - The except block catches the exception and prints the error message.
# -------------------------------------------------------------


# -------------------------------------------------------------
# Summary:
# 1. Selenium actions are placed inside try block.
# 2. NoSuchElementException occurs when an element is not found.
# 3. except block prevents test crash.
# 4. Proper exception handling improves test stability.
# -------------------------------------------------------------
