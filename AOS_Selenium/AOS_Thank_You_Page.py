from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Thank_You_Page:
    def __init__(self, driver: webdriver.Chrome):
        """Initialize the Thank_You_Page class with a Selenium WebDriver instance."""

        self.driver = driver

    def order_confirmation(self):
        """Return the order confirmation element."""
        return self.driver.find_element(By.CSS_SELECTOR, '[translate="Thank_you_for_buying_with_Advantage"]')

    def get_confirmation_text(self):
        """Return the text of the order confirmation element."""
        return self.order_confirmation().get_attribute("innerHTML")

    def order_number(self):
        """Return the order number element."""
        return self.driver.find_element(By.ID, "orderNumberLabel")

    def wait_for_order_number(self):
        """Wait until the order number element is visible."""
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, "orderNumberLabel")))

    def get_order_number_text(self):
        """Return the text of the order number element."""
        return self.order_number().get_attribute("innerHTML")

    def tracking_number(self):
        """Return the tracking number element."""
        return self.driver.find_element(By.ID, "trackingNumberLabel")


