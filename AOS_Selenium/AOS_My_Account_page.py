from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class My_Account_Page:
    def __init__(self, driver: webdriver.Chrome):
        """Initialize the My_Account_Page class with a Selenium WebDriver instance."""
        self.driver = driver

    def delete(self):
        """Return the delete button element."""
        return self.driver.find_element(By.CLASS_NAME, "deleteBtnText")

    def confirm_deletion(self):
        """Wait until the confirm deletion button is visible and return the element."""
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".deleteRed")))
        return self.driver.find_element(By.CSS_SELECTOR, ".deleteRed")
