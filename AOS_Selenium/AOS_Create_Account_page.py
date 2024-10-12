from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep


class Create_Account_Page:
    def __init__(self, driver: webdriver.Chrome):
        """Initialize the Create_Account_Page class with a Selenium WebDriver instance."""
        self.driver = driver

    def name_field(self):
        """Return the name input field element."""
        return self.driver.find_element(By.NAME, "usernameRegisterPage")

    def type_name(self, name: str):
        """Type the name into the name input field."""
        self.name_field().send_keys(name)

    def get_name_value(self):
        """Return the value of the name input field."""
        return self.name_field().get_attribute("value")

    def email_field(self):
        """Return the email input field element."""
        return self.driver.find_element(By.NAME, "emailRegisterPage")

    def type_email(self, email: str):
        """Type the email into the email input field."""
        self.email_field().send_keys(email)

    def get_email_value(self):
        """Return the value of the email input field."""
        return self.email_field().get_attribute("value")

    def password_field(self):
        """Return the password input field element."""
        return self.driver.find_element(By.NAME, "passwordRegisterPage")

    def type_password(self, password: str):
        """Type the password into the password input field."""
        self.password_field().send_keys(password)

    def get_password_value(self):
        """Return the value of the password input field."""
        return self.password_field().get_attribute("value")

    def confirm_password_field(self):
        """Return the confirmation password input field element."""
        return self.driver.find_element(By.NAME, "confirm_passwordRegisterPage")

    def type_confirm_password(self, password: str):
        """Type the password into the confirmation password input field."""
        self.confirm_password_field().send_keys(password)

    def get_confirm_password_value(self):
        """Return the value of the confirmation password input field."""
        return self.confirm_password_field().get_attribute("value")

    def choose_country(self, country):
        """Select the country from the dropdown list."""
        country_element = self.driver.find_element(By.NAME, "countryListboxRegisterPage")
        country_dropdown = Select(country_element)
        country_dropdown.select_by_visible_text(country)

    def condition_of_use(self):
        """Return the condition of use checkbox element."""
        return self.driver.find_element(By.NAME, "i_agree")

    def register_btn(self):
        """Return the register button element."""
        return self.driver.find_element(By.ID, "register_btn")



