# START REQUIRED IMPORTS ----------------------------------------------------------------------------


import pytest
import time
from pages.login_page import LoginPage
from pages.campaign_page import Campaign
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import logging
# END IMPORTS HERER ----------------------------------------------------------------------------------


logger = logging.getLogger()

# Constants
CALLHUB_LOGIN = 'https://app.callhub.io/login'


# Scenarios
scenarios('../features/script_validation.feature')


# Given Steps
@given('the CallHub login page is displayed')
def callhub_home(driver):
    """ launching callhub login page """
    logger.error("Starting test for script text validation while creating text broadcast campaign")
    driver.get(CALLHUB_LOGIN)

# When Steps
@when(parsers.parse('the user logs in using valid "{username}" and "{password}"'))
def callhub_login(driver, username, password):
    """ logging in to user account with valid username and password """
    login_page = LoginPage(driver)
    login_page.set_username(username)
    login_page.click_next_after_username()
    login_page.set_password(password)
    login_page.click_final_log_in()


@when(parsers.parse('user starts creating campaign using phonebook "{phonebook}"'))
def create_campaign(driver, phonebook):
    """ starting campaign creation """
    campaign = Campaign(driver)
    campaign.click_create_text_broadcast()
    campaign.click_phonebook_dropdown()
    campaign.click_phonebook(phonebook)



@when('user does not type any script for text broadcast')
def click_next_button(driver):
    """ clicking on next button without any script text for broadcast """
    campaign = Campaign(driver)
    campaign.click_button(wait=False)
    campaign.click_button()

    

@then(parsers.parse('error message "{error_message}" should be shown on the screen'))
def script_validation(driver, error_message):
    """ validating the script without any text for broadcast """
    campaign = Campaign(driver)
    message = campaign.get_error_msg()
    assert message == error_message, 'Script validation failed!!!'
    logger.error("Script validation test successful....... ")


