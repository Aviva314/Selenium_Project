from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class Home_page:
    def __init__(self, driver: webdriver.Chrome):
        """Initialize the Home_page class with a Selenium WebDriver instance."""
        self.driver = driver

    def categories(self):
        """Return all category elements on the homepage."""
        return self.driver.find_elements(By.CSS_SELECTOR, ".categoryCell")

    def category_click(self, i: int):
        """Click a specific category by index."""
        self.categories()[i].click()

    def category_by_id(self, i: str):
        """Return a category element by its ID."""
        return self.driver.find_element(By.ID, i)

    def category_by_id_click(self, i: str):
        """Click a specific category by its ID."""
        self.category_by_id(i).click()


