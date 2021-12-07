# START REQUIRED IMPORTS ----------------------------------------------------------------------------

import pytest
import time
from pages.login_page import LoginPage # importing LoginPage class 
from pages.campaign_page import Campaign   # importing Campaign class
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException # for error handling
import logging

# END IMPORTS HERER ----------------------------------------------------------------------------------

logger = logging.getLogger()


# Constants

CALLHUB_LOGIN = 'https://app.callhub.io/login'


# Scenarios 
scenarios('../features/phonebook_validation.feature')


# Given Steps
@given('the CallHub login page is displayed')
def callhub_home(driver):
    """ launching the callhub Login Page   """
    logger.error("Starting test for phonebook validation while creating text broadcast campaign")
    driver.get(CALLHUB_LOGIN)

# When Steps
@when(parsers.parse('the user logs in using valid "{username}" and "{password}"'))
def callhub_login(driver, username, password):
    """ logging in user account   """
    login_page = LoginPage(driver)
    login_page.set_username(username)
    login_page.click_next_after_username()
    login_page.set_password(password)
    login_page.click_final_log_in()


@when('user starts creating campaign')
def create_campaign(driver):
    """ starting campaign creation  """
    campaign = Campaign(driver)
    campaign.click_create_text_broadcast()


@when('user does not select any phonebook')
def click_next_button(driver):
    """  clicking next button on Targetting  """
    campaign = Campaign(driver)
    campaign.click_button(wait=False)



@then(parsers.parse('error message "{error_message}" should be shown on the screen'))
def phonebook_validation(driver, error_message):
    """  Validation without selecting any phonebook  """
    campaign = Campaign(driver)
    message = campaign.get_error_msg()
    assert  message == error_message, 'Phonebook validation failed!!!'
    logger.error("Phonebook validation test successful....... ")
    


