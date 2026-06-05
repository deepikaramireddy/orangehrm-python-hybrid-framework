from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage


class TestLogin:
    baseURL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    USERNAME = "Admin"
    PASSWORD = "admin123"

    def test_successful_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        self.login_page = LoginPage(self.driver)

        # Wait for the login fields to load dynamically
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(LoginPage.USERNAME_INPUT))

        # Enter credentials and log in
        self.login_page.enter_username(self.USERNAME)
        self.login_page.enter_password(self.PASSWORD)
        self.login_page.click_login_button()

