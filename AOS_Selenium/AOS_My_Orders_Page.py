from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class My_Orders_Page:
    def __init__(self, driver: webdriver.Chrome):
        """Initialize the My_Orders_Page class with a Selenium WebDriver instance."""
        self.driver = driver

    def order_number(self):
        """Return all order number elements."""
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'nav>a[translate="MY_ORDERS"]')))
        return self.driver.find_elements(By.XPATH, '//*[@id="myAccountContainer"]/div/table/tbody/tr/td[1]/label')














#//*[@id="myAccountContainer"]/div/table/tbody/tr/td[1]/label

# a path for the list of order numbers