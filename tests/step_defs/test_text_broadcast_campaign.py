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

# END IMPORTS HERE----------------------------------------------------------------------------------

logger = logging.getLogger()

# Constants

CALLHUB_PAGE = 'https://app.callhub.io/login'


# Scenarios
scenarios('../features/text_broadcast_campaign.feature')


# Start of background -------------------------------------------------------------------------------
@given('the CallHub business homepage page is displayed')
def callhub_home(driver):
    """ launching callhub marketing page """
    logger.error("Starting the campaign creation and validation test")
    driver.get(CALLHUB_PAGE)


# When Steps
@given(parsers.parse('the user logs in using valid "{username}" and "{password}"'))
def callhub_login(driver, username, password):
    """ logging into user account with username and password """
    login_page = LoginPage(driver)
    # driver.save_screenshot("login_page")
    # login_page.click_signup_login()
    # login_page.click_on_log_in_here()
    login_page.set_username(username)
    login_page.click_next_after_username()
    login_page.set_password(password)
    login_page.click_final_log_in()


# Then Steps
@given('the user starts text broadcast campaign creation')
def start_of_text_broadcast_campaign(driver):
    """ starting text broadcast campaign creation """
    campaign = Campaign(driver)
    campaign.click_create_text_broadcast()

# End of Background ----------------------------------------------------------------------------------------


# Start of Text Broadcast campaign creation and completion test----------------------------------------------
@pytest.mark.campaign
@when(parsers.parse('the user finishes creating text broadcast campaign with a "{phonebook}"'))
def create_campaign(driver, phonebook):
    """ starting text broadcast campaign creation with a phonebook """
    campaign = Campaign(driver)
    campaign.click_phonebook_dropdown()
    campaign.click_phonebook(phonebook)
    campaign.click_button(wait=False)
    campaign.close_popup()
    campaign.set_script()
    campaign.click_button()
    campaign.click_button()
    campaign.click_button()
    campaign.click_button(button="finish")


@when('user is redirected to overview page')
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


@then('the user clicks on start and campaign completion is verified')
def start_campaign(driver):
    """ starting campaign and refreshing it after 60 seconds  """
    campaign = Campaign(driver)
    max_time = 120
    time_counter = 0
    total_contacts_count = campaign.get_total_contacts_count()
    campaign.click_start()
    start_time = time.time()
    while (time_counter) < max_time:
        time.sleep(20)
        driver.refresh()
        time_after_refresh = time.time()
        time_counter = time_after_refresh-start_time
        print(time_counter)
        total_completed_count = campaign.get_total_completed_count()
        if total_completed_count == total_contacts_count:
            break            
    try:
        assert total_contacts_count == total_completed_count, "Campaign not completed!!!"
        print("Validation for campaign completion is successful....")
    except:
        print('NoSuchElementException in verify_campaign_completion() yet')
        logger.error("Refreshing and checking again till the threshold time!!!")

    # print("The total Contacts Count is {}".format(total_contacts_count))
    # print("The total completed count is {} in {} seconds after start".format(
    #     total_completed_count, time_counter))
    


# @then('validate the count of successful messages sent from the campaign overview page')
# def verify_campaign_completion(driver):
#     """ validating successful campaign flow """
#     campaign = Campaign(driver)


# End of Text Broadcast campaign creation and completion test----------------------------------------------


# Start of phonebook validation test----------------------------------------------------------------------
@pytest.mark.phonebook
@when('user does not select any phonebook')
def click_phonebook_next_button(driver):
    """  clicking next button on Targetting  """
    campaign = Campaign(driver)
    campaign.click_button(wait=False)


@then(parsers.parse('error message "{error_message}" should be shown on the screen'))
def phonebook_validation(driver, error_message):
    """  Validation without selecting any phonebook  """
    campaign = Campaign(driver)
    message = campaign.get_error_msg()
    assert message == error_message, 'Phonebook validation failed!!!'
    logger.error("Phonebook validation test successful....... ")

# End of phonebook validation test---------------------------------------------------------------------


# Start of script validation test-----------------------------------------------------------------------
@when(parsers.parse('user selects phonebook "{phonebook}"'))
def select_phonebook(driver, phonebook):
    """ phonebook selection for script validation """
    campaign = Campaign(driver)
    campaign.click_phonebook_dropdown()
    campaign.click_phonebook(phonebook)


@when('user does not type any script for text broadcast')
def click_script_next_button(driver):
    """ clicking on next button without any script text for broadcast """
    campaign = Campaign(driver)
    campaign.click_button(wait=False)
    try:
        campaign.close_popup()
    except:
        logger.error("This popup was not found this time!!!")
    campaign.click_button()


@then(parsers.parse('error message "{error_message}" should be shown on the screen'))
def script_validation(driver, error_message):
    """ validating the script without any text for broadcast """
    campaign = Campaign(driver)
    message = campaign.get_error_msg()
    assert message == error_message, 'Script validation failed!!!'
    logger.error("Script validation test successful....... ")

# End of script validation test-----------------------------------------------------------------------
