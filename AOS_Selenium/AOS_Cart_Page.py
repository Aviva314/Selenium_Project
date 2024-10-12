from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Cart_Page:
    def __init__(self, driver: webdriver.Chrome):
        """Initialize the Cart_Page class with a Selenium WebDriver instance."""
        self.driver = driver

    def empty_cart(self):
        """Wait until the "continue shopping" element is visible and return the empty cart text element."""
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[translate="CONTINUE_SHOPPING"]')))
        return self.driver.find_element(By.XPATH, "//div[3]/section/article/div[1]/div/label")

    def total_price_cart(self):
        """Return the total price element."""
        return self.driver.find_element(By.XPATH, "//tfoot/tr/td[2]/span[2]")

    def table_rows_products_in_cart(self):
        """Return all product rows in the cart."""
        table = self.driver.find_element(By.CSS_SELECTOR, "table.fixedTableEdgeCompatibility")
        product_rows = table.find_elements(By.CSS_SELECTOR, "tbody>tr")
        return product_rows

    def row_columns_in_cart(self, i):
        """Return the columns of a specific product row in the cart."""
        return self.table_rows_products_in_cart()[i].find_elements(By.TAG_NAME, "td")

    def product_name(self, i):
        """Return the product name element as text of a specific product in the cart."""
        return self.row_columns_in_cart(i)[1].find_element(By.TAG_NAME, "label").text

    def product_color(self, i):
        """Return the product color element of a specific product in the cart."""
        return self.row_columns_in_cart(i)[3].find_element(By.TAG_NAME, "span")

    def get_color_by_title(self, i):
        """Return the color of a specific product in the cart by its title attribute."""
        return self.product_color(i).get_attribute("title")

    def product_quantity(self, i):
        """Return the product quantity element as text of a specific product in the cart."""
        return self.row_columns_in_cart(i)[4].find_element(By.CLASS_NAME, "ng-binding").text

    def product_price(self, i):
        """Return the product price element as text of a specific product in the cart."""
        return self.row_columns_in_cart(i)[5].find_element(By.TAG_NAME, "p").text

    def edit_button(self, i):
        """Return the edit button element for a specific product row in the cart."""
        return self.row_columns_in_cart(i)[5].find_element(By.CSS_SELECTOR, ".edit")

    def remove_button(self, i):
        """Return the remove button element for a specific product row in the cart."""
        return self.row_columns_in_cart(i)[5].find_element(By.CSS_SELECTOR, ".remove")

    def checkout_button(self):
        """Return the checkout button element."""
        return self.driver.find_element(By.ID, "checkOutButton")

    def wait_for_shopping_cart_page(self):
        """Wait until the shopping cart page is fully loaded,
        when the "shopping cart" text is visible on the navigation bar."""
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="select  ng-binding"]')))
