from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Sign_In_Window:
    def __init__(self, driver: webdriver.Chrome):
        """Initialize the Tool_Bar class with a Selenium WebDriver instance."""
        self.driver = driver

    def log_in_elements(self):
        """Return sing in window elements."""
        return self.driver.find_elements(By.XPATH,
                                         '//*[@name="username"] | //*[@name="password"] | //*[@name="remember_me"]')

    def type_log_in_element(self, i, string: str):
        """Type  into the input fields by index."""
        return self.log_in_elements()[i].send_keys(string)

    def username(self):
        """Return the username input field element."""
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "animated")))
        return self.driver.find_element(By.NAME, "username")

    def type_username(self, username: str):
        """Type the username into the username input field."""
        self.username().send_keys(username)

    def type_username_java(self, username: str):
        """Type the username into the username input field using JavaScript."""
        self.driver.execute_script(f"arguments[0].value = '{username}';", self.username())

    def password(self):
        """Return the password input field element."""
        return self.driver.find_element(By.NAME, "password")

    def type_password(self, password: str):
        """Type the password into the password input field."""
        self.password().send_keys(password)

    def remember_me(self):
        """Return the "Remember Me" check box element."""
        return self.driver.find_element(By.NAME, "remember_me")

    def sign_in(self):
        """Return the sign-in button element."""
        wait = WebDriverWait(self.driver, 10)
        sign_in = wait.until(EC.element_to_be_clickable((By.ID, "sign_in_btn")))
        return sign_in

    def create_new_account_button(self):
        """Return the "create new account" "element."""
        return self.driver.find_element(By.CSS_SELECTOR, '[translate="CREATE_NEW_ACCOUNT"]')


