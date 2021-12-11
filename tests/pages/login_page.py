from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from step_defs.conftest import highlight
import time



class LoginPage:

    """ functions for login page """

    def __init__(self, driver):
        self.driver = driver

    def click_signup_login(self):
        login_button = self.driver.find_element(By.ID, 'getStarted')
        self.driver.implicitly_wait(60)
        highlight(login_button)
        ActionChains(self.driver).move_to_element(
            login_button).click(login_button).perform()

    def click_on_log_in_here(self):
        log_in_here = self.driver.find_element(By.XPATH,
                                 "//a[@href='https://app.callhub.io/login/' and text()='Log in here']")
        highlight(log_in_here)
        log_in_here.click()


    def set_username(self, username):
        username_field = self.driver.find_element(By.ID, "id_user")
        highlight(username_field)
        username_field.send_keys(username)
        return username_field

    def click_next_after_username(self):
        next_button = self.driver.find_element(By.ID, 'change-btn-text')
        highlight(next_button)
        next_button.click()

    def set_password(self, password):
        password_field = self.driver.find_element(By.ID, 'id_password')
        highlight(password_field)
        password_field.send_keys(password)
        time.sleep(5)

    def click_final_log_in(self):
        sign_in_button = self.driver.find_element(By.ID, 'change-btn-text')
        highlight(sign_in_button)
        sign_in_button.click()

    def verify_login(self):
        return self. driver.find_element(By.XPATH, '//li[@page="guide"]').is_displayed()


    




# a = [15,20,11,5,2]
# max_num = 0
# for i in a:
#    if  i > max_num:
#        max_num = i

# print (max_num)




