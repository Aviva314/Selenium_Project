from selenium import webdriver
from selenium.webdriver.common.by import By


class Product_Page:
    def __init__(self, driver: webdriver.Chrome):
        """Initialize the Product_Page class with a Selenium WebDriver instance."""
        self.driver = driver

    def colors(self):
        """Return all product color elements."""
        return self.driver.find_elements(By.CSS_SELECTOR, '.colors>[class=""]>span')

    def get_color_title(self, i: int):
        """Return the title attribute value of a specific color element."""
        return self.colors()[i].get_attribute("title").strip()

    def color(self, title: str):
        """Return product color element by title"""
        color = self.driver.find_element(By.CSS_SELECTOR,
                                         f"div>[ng-show='firstImageToShow']>[title='{title.upper()}']")
        return color

    def quantity(self):
        """Return the quantity input field element."""
        return self.driver.find_element(By.NAME, "quantity")

    def plus_click(self):
        """Click the plus button to increase the quantity."""
        return self.driver.find_element(By.CLASS_NAME, "plus").click()

    def minus_click(self):
        """Click the minus button to decrease the quantity."""
        return self.driver.find_element(By.CLASS_NAME, "minus").click()

    def add_to_cart(self):
        """Return the 'add to cart' button element."""
        return self.driver.find_element(By.NAME, "save_to_cart")

    def add_to_cart_click(self):
        """Click on 'add to cart' button"""
        return self.add_to_cart().click()

    def type_quantity(self, quantity: str):
        """Type the quantity into the quantity input field after clearing the previous input."""
        quantity_field = self.quantity()
        self.driver.execute_script("arguments[0].value = '';", quantity_field)  # Clear the field using JavaScript
        quantity_field.send_keys(quantity)
        # self.quantity().clear()
        # self.quantity().send_keys(quantity)

    def get_quantity_value(self):
        """Return the value of the quantity input field."""
        return self.quantity().get_attribute("value")

    def product_description(self):
        """Return the product description element."""
        return self.driver.find_element(By.CSS_SELECTOR, "div#Description>h1")

    def price(self):
        """Return the price element."""
        return self.driver.find_element(By.CSS_SELECTOR, "div#Description>h2")

    def out_of_stock(self):
        """Return the 'out of stock' element."""
        return self.driver.find_element(By.CSS_SELECTOR, "#Description>h2>span")


