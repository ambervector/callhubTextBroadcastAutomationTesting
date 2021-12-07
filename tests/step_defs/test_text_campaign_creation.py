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

CALLHUB_PAGE = 'https://callhub.io/'


# Scenarios
scenarios('../features/text_campaign_creation.feature')


# Given Steps
@given('the CallHub homepage page is displayed')
def callhub_home(driver):
    """ launching callhub marketing page """
    logger.error("Starting the campaign creation and validation test")
    driver.get(CALLHUB_PAGE)


# When Steps
@when(parsers.parse('the user logs in using valid "{username}" and "{password}"'))
def callhub_login(driver, username, password):
    """ logging into user account with username and password """
    login_page = LoginPage(driver)
    # driver.save_screenshot("login_page")
    login_page.click_signup_login()
    login_page.click_on_log_in_here()
    login_page.set_username(username)
    login_page.click_next_after_username()
    login_page.set_password(password)
    login_page.click_final_log_in()


# Then Steps
@then('the user is redirected to the guide page')
def verify_login(driver):
    """ validating succesful user log in """
    login_page = LoginPage(driver)
    present = login_page.verify_login()
    assert present == True, "Login Failed !!!"



@when(parsers.parse('the user finishes creating text broadcast campaign with a phonebook called "{phonebook}"'))
def create_campaign(driver, phonebook):
    """ starting campaign creation with a phonebook """
    campaign = Campaign(driver)
    campaign.click_create_text_broadcast()
    campaign.click_phonebook_dropdown()
    campaign.click_phonebook(phonebook)
    campaign.click_button(wait=False)
    campaign.set_script()
    campaign.click_button()
    campaign.click_button()
    campaign.click_button()
    campaign.click_button(button="finish")


@then('user is redirected to overview page')
def verify_campaign_creation(driver):
    """ verifying successful campaign creation """
    campaign = Campaign(driver)
    try:
        text = campaign.get_overview_text()
        assert text == 'Overview', "Campaign creation failed!!!"
        time.sleep(5)
    except NoSuchElementException as error:
        print("NoSuchElementException in verify_campaign_creation()" + error.msg)
    logger.error("Ending the campaign creation")


@when('the user clicks on start')
def start_campaign(driver):
    """ starting campaign and refreshing it after 60 seconds  """
    campaign = Campaign(driver)
    campaign.click_start_and_refresh()


@then('validate the count of successful messages sent from the campaign overview page')
def verify_campaign_completion(driver):
    """ validating successful campaign flow """
    campaign = Campaign(driver)
    try:
        total_contacts_count = campaign.get_total_contacts_count()
        print(total_contacts_count,
              "This is the extracted string from Contacts Count")
        total_completed_count = campaign.get_total_completed_count()
        assert total_contacts_count == total_completed_count, "Campaign not completed!!!"
        time.sleep(5)
        logger.error("Validation for campaign completion is successful....")
    except NoSuchElementException as error:
        print('NoSuchElementException in verify_campaign_completion()' + error.msg)
    

   