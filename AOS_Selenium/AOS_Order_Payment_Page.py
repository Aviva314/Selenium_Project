from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Order_Payment_Page:
    def __init__(self, driver: webdriver.Chrome):
        """Initialize the Order_Payment_Page class with a Selenium WebDriver instance."""
        self.driver = driver

    def username(self):
        """Return the username input field element."""
        return self.driver.find_element(By.NAME, "usernameInOrderPayment")

    def type_username(self, username: str):
        """Type the username into the username input field."""
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                     '[class="roboto-regular sticky fixedImportant ng-scope"]')))
        self.username().send_keys(username)

    def password(self):
        """Return the password input field element."""
        return self.driver.find_element(By.NAME, "passwordInOrderPayment")

    def type_password(self, password: str):
        """Type the password into the password input field."""
        self.password().send_keys(password)

    def login(self):
        """Return the login button element."""
        return self.driver.find_element(By.ID, "login_btn")

    def registration(self):
        """Return the registration button element."""
        return self.driver.find_element(By.ID, "registration_btn")

    def edit_shipping_details(self):
        """Return the 'Edit shipping details' link element."""
        return self.driver.find_element(By.LINK_TEXT, "Edit shipping details")

    def next(self):
        """Return the next button element."""
        return self.driver.find_element(By.CSS_SELECTOR, "div>#next_btn")

    def safepay(self):
        """Return the SafePay payment option element."""
        return self.driver.find_element(By.NAME, "safepay")

    def safepay_username(self):
        """Return the SafePay username input field element."""
        return self.driver.find_element(By.NAME, "safepay_username")

    def type_safepay_username(self, username: str):
        """Type the SafePay username into the SafePay username input field."""
        self.safepay_username().send_keys(username)

    def get_safepay_username(self):
        """Return the value of the SafePay username input field."""
        return self.safepay_username().get_attribute("value")

    def safepay_password(self):
        """Return the SafePay password input field element."""
        return self.driver.find_element(By.NAME, "safepay_password")

    def type_safepay_password(self, password: str):
        """Type the SafePay password into the SafePay password input field."""
        self.safepay_password().send_keys(password)

    def get_safepay_password(self):
        """Return the value of the SafePay password input field."""
        return self.safepay_password().get_attribute("value")

    def save_safepay_payment_changes(self):
        """Return the 'Save changes' button element for SafePay payment."""
        return self.driver.find_element(By.NAME, "save_safepay")

    def creditcard(self):
        """Return the credit card payment option element."""
        return self.driver.find_element(By.NAME, "masterCredit")

    def card_number(self):
        """Return the card number input field element."""
        return self.driver.find_element(By.NAME, "card_number")

    def type_card_number(self, num: str):
        """Type the card number into the card number input field."""
        self.card_number().send_keys(num)

    def cvv_number(self):
        """Return the CVV number input field element."""
        return self.driver.find_element(By.NAME, "cvv_number")

    def type_cvv_number(self, num: str):
        """Type the CVV number into the CVV number input field."""
        self.cvv_number().send_keys(num)

    def expiration_month(self):
        """Return the expiration month dropdown element."""
        return self.driver.find_element(By.NAME, "mmListbox")

    def choose_expiration_month(self, month: str):
        """Select the expiration month from the dropdown list."""
        month_dropdown = Select(self.expiration_month())
        month_dropdown.select_by_visible_text(month)

    def expiration_year(self):
        """Return the expiration year dropdown element."""
        return self.driver.find_element(By.NAME, "yyyyListbox")

    def choose_expiration_year(self, year: str):
        """Select the expiration year from the dropdown list."""
        year_dropdown = Select(self.expiration_year())
        year_dropdown.select_by_visible_text(year)

    def card_holder(self):
        """Return the cardholder input field element."""
        return self.driver.find_element(By.NAME, "cardholder_name")

    def type_card_holder(self, name: str):
        """Type the cardholder name into the cardholder input field."""
        self.card_holder().send_keys(name)

    def save_card_payment_changes(self):
        """Return the 'Save changes' button element for credit card payment."""
        return self.driver.find_element(By.NAME, "save_master_credit")

    def back_to_shipping_details(self):
        """Return the 'Back to shipping details' link element."""
        return self.driver.find_elements(By.LINK_TEXT, "Back to shipping details")[2]

    def pay_now_safepay(self):
        """Return the 'Pay Now' button element for SafePay payment."""
        return self.driver.find_element(By.ID, "pay_now_btn_SAFEPAY")

    def pay_now_card(self):
        """Return the 'Pay Now' button element for credit card payment."""
        return self.driver.find_element(By.ID, "pay_now_btn_ManualPayment")


