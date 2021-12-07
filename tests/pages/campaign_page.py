# START REQUIRED IMPORTS ----------------------------------------------------------------------------


import time
from pages.login_page import highlight
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# END IMPORTS HERER ----------------------------------------------------------------------------------


class Campaign:
    """ functions for campaign creation and validation """
    def __init__(self, driver):
        self.driver = driver

    def click_create_text_broadcast(self):
        create_button = self.driver.find_element(By.XPATH,
                                                 "//a[@href='/smsbroadcast/create/']")
        highlight(create_button)
        create_button.click()
        time.sleep(5)

    def click_phonebook_dropdown(self):
        phonebook_dropdown = self.driver.find_element(By.CLASS_NAME,
                                                      "css-1wa3eu0-placeholder")
        highlight(phonebook_dropdown)
        phonebook_dropdown.click()
        time.sleep(5)

    def click_phonebook(self, phonebook):
        phonebook_element = self.driver.find_element(
            By.XPATH, "//*[text()='"+phonebook+"']")
        highlight(phonebook_element)
        ActionChains(self.driver).key_down(Keys.DOWN).click(
            phonebook_element).key_up(Keys.DOWN).perform()
        time.sleep(5)

    def click_button(self, button='next', wait=True):
        next_button = self.driver.find_element(
            By.XPATH, "//button[text()='"+button+"']")

        if wait:
            highlight(next_button)
            self.driver.execute_script("arguments[0].click();", WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='"+button+"']"))))
        else:
            # next_button = self.driver.find_element(
            #     By.XPATH, "//button[text()='"+button+"']")
            self.driver.execute_script(
                "arguments[0].scrollIntoView();", next_button)
            # highlight(next_button)
            highlight(next_button)

            next_button.click()
        time.sleep(3)

    def set_script(self):
        script_field = self.driver.find_element(By.ID, 'message-textarea')
        highlight(script_field)
        script_field.send_keys('Test')
        time.sleep(5)

    def get_overview_text(self):
        return self.driver.find_element(By.XPATH, "//span[text()='Overview']").text

    def click_start_and_refresh(self):
        start_button = self.driver.find_element(
            By.XPATH, '(//div/button[@class="button-style rounded-left btn-border-right"])[1]')
        highlight(start_button)
        start_button.click()
        time.sleep(60)
        self.driver.refresh()
        time.sleep(5)

    def get_total_contacts_count(self):
        total_contacts = self.driver.find_element(By.CSS_SELECTOR, 'span.undefined > sub >span')
        highlight(total_contacts)
        return total_contacts.text

    def get_total_completed_count(self):
        total_completed_count = self.driver.find_element(
            By.XPATH, '(//div[@class="caption-label"])[1]')
        highlight(total_completed_count)
        extracted_text = total_completed_count.text
        print(extracted_text, "This is the extracted string from Completed Count")
        return extracted_text[0]

    def get_error_msg(self):
        error = self.driver.find_element(By.CSS_SELECTOR, 'p.error-message-text')
        highlight(error)
        return error.text
