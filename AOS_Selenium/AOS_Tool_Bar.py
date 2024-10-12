from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class Tool_Bar:
    def __init__(self, driver: webdriver.Chrome):
        """Initialize the Tool_Bar class with a Selenium WebDriver instance."""
        self.driver = driver

    def logo(self):
        """Return the logo element on the page."""
        return self.driver.find_element(By.CSS_SELECTOR, ".logo>a")

    def logo_click(self):
        """Wait until the logo is clickable and then click it."""
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='#/']")))
        self.logo().click()

    def header_elements(self):
        """Return all header elements on the page in a list."""
        return self.driver.find_elements(By.CSS_SELECTOR, "header>nav>ul>li")

    def header_element_click(self, i):
        """Click a specific header element by index."""
        self.header_elements()[i].click()

    def navigation_bar(self):
        """Return navigation toolbar elements"""
        return self.driver.find_elements(By.CSS_SELECTOR, "nav>a")

    def cart_click(self):
        """Click the shopping cart element."""
        self.driver.find_element(By.ID, "shoppingCartLink").click()

    def wait_for_cart_preview(self):
        """Wait until the cart icon is visible."""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "menuCart")))

    def cart_preview(self):
        """Hover over the cart icon to display the cart preview."""
        cart_icon = self.driver.find_element(By.ID, "shoppingCartLink")
        action_chain = ActionChains(self.driver)
        # Move to element
        action_chain.move_to_element(cart_icon).perform()

    def total_items_in_cart_preview(self):
        """Return the total number of items element in the cart preview."""
        num_items = self.driver.find_elements(By.CSS_SELECTOR, "td>span>label")
        self.cart_preview()
        return num_items[0]

    def table_rows_products_in_cart_preview(self):
        """Return all product rows in cart preview"""
        return self.driver.find_elements(By.CSS_SELECTOR, "table>tbody>tr")

    def row_columns_cart_preview(self, i):
        """Return the columns of a specific product in the cart preview"""
        product_rows = self.table_rows_products_in_cart_preview()[i].find_elements(By.TAG_NAME, "td")
        return product_rows

    def product_description_cart_preview(self, i):
        """ Return the product description for a specific product in the cart preview as text."""
        return self.row_columns_cart_preview(i)[1].find_element(By.CSS_SELECTOR, "a>h3").text

    def quantity_cart_preview(self, i):
        """Return the quantity of a specific product in the cart preview as text."""
        return self.row_columns_cart_preview(i)[1].find_elements(By.CSS_SELECTOR, "a>label")[0].text[5:]

    def color_cart_preview(self, i):
        """Return the color of a specific product in the cart preview as text."""
        return self.row_columns_cart_preview(i)[1].find_elements(By.CSS_SELECTOR, "a>label")[1].text[7:]

    def price_cart_preview(self, i):
        """Return the price of a specific product in the cart preview."""
        return self.row_columns_cart_preview(i)[2].find_element(By.CSS_SELECTOR, "p").text[1:].replace(",", "")

    def remove_product_cart_preview(self, i):
        """Return the remove button for a specific product row in the cart preview."""
        return self.row_columns_cart_preview(i)[2].find_element(By.CSS_SELECTOR, "div>div.removeProduct")

    def checkout(self):
        """Return the checkout button element in the cart preview."""
        return self.driver.find_element(By.ID, "checkOutPopUp")

    def wait_to_menu_user(self):
        """Wait until the user menu is clickable after login."""
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#menuUserLink>span")))

    def wait_for_user_to_disappear(self):
        """Wait until the username element disappears after logging out."""
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, "#menuUserLink>span")))

    def menu_user(self):
        """Return the username element on the upper navigation bar."""
        return self.driver.find_element(By.CSS_SELECTOR, "#menuUserLink>span")

    def get_menu_user(self):
        """Return the username element on the upper navigation bar as text using innerHTML."""
        return self.menu_user().get_attribute("innerHTML")

    def account_icon(self):
        """Return the account icon element."""
        return self.driver.find_element(By.ID, "menuUser")

    def account_icon_click(self):
        """Wait until the account icon is clickable and then click it."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "menuUser"))
        ).click()

    def my_orders_button(self):
        """Return the "My Orders" element in the account dropdown."""
        return self.driver.find_element(By.XPATH, '//li[3]/a/div/label[2]')

    def my_account_button(self):
        """Return the "My Account" element in the account dropdown."""
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//li[3]/a/div/label[1]')))
        return self.driver.find_element(By.XPATH, '//li[3]/a/div/label[1]')

    def sign_out(self):
        """""Return the "Sign Out" element in the account dropdown."""
        return self.driver.find_element(By.XPATH, '//li[3]/a/div/label[3]')
