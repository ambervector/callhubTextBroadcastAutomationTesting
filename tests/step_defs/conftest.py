"""
This module contains shared fixtures, steps, and hooks.
"""
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Fixtures


@pytest.fixture
def driver():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.maximize_window()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
