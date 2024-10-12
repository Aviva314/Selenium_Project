from selenium import webdriver
from selenium.webdriver.common.by import By


class Category_Page:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def items(self):
        """Initialize the Category_Page class with a Selenium WebDriver instance."""
        return self.driver.find_elements(By.CSS_SELECTOR, "ul>li>img")

    def get_item_id_value(self, i):
        """Return the ID attribute value of a specific item element."""
        return self.items()[i].get_attribute("id")

    def items_click(self, i):
        """Click a specific item by index."""
        self.items()[i].click()

    def item_by_id_click(self, i: str):
        """Return a product by ID and click it"""
        return self.driver.find_element(By.ID, i).click()




