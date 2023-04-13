from django.contrib.auth import get_user_model
from django.conf import settings

from selenium.webdriver.common.by import By

from protected657.tests.utils import SeleniumChromeTestCase

User = get_user_model()


class ProtectedFilesAdminUserTest(SeleniumChromeTestCase):

    USERNAME = "testare"
    PASSWORD = "password1234"
    UPLOADFILE = f"{settings.BASE_DIR}/protected657/tests/door_logo43.png"

    def setUp(self):
        # Create a user to login with
        user = User.objects.create_user(
            username=self.USERNAME,
            email="test@example.com",
            password=self.PASSWORD,
            is_staff=True,
        )
        self.selenium.get(f"{self.live_server_url}/admin/login/")
        self.selenium.implicitly_wait(0.5)
        login_form = self.selenium.find_element(by=By.ID, value="login-form")
        username = login_form.find_element(by=By.NAME, value="username")
        username.send_keys(self.USERNAME)
        username = login_form.find_element(by=By.NAME, value="password")
        username.send_keys(self.PASSWORD)
        submit_row = login_form.find_element(by=By.CLASS_NAME, value="submit-row")
        submit_button = submit_row.find_element(by=By.CSS_SELECTOR, value="input")
        submit_button.click()
        self.selenium.implicitly_wait(0.5)
        assert self.selenium.title == "Webbplatsadministration | Django webbplatsadministration"
    
    def testLandingpage(self):
        self.selenium.get(f"{self.live_server_url}/")
        self.selenium.implicitly_wait(0.5)

    def testProtectedFiles(self):
        self.selenium.get(f"{self.live_server_url}/protected/")
        self.selenium.implicitly_wait(0.5)
        assert "Protected files" in self.selenium.page_source

    def testProtectedFilesAdd(self):
        self.selenium.get(f"{self.live_server_url}/protected/add/")
        self.selenium.implicitly_wait(0.5)
        assert "Add File" in self.selenium.page_source
        title_input = self.selenium.find_element(by=By.ID, value="id_title")
        title_input.send_keys("Selenium test")
        self.selenium.find_element(By.ID,"id_file").send_keys(self.UPLOADFILE)
        self.selenium.find_element(By.TAG_NAME, "button").submit()
        self.selenium.implicitly_wait(0.5)
        assert self.selenium.page_source.find("Selenium test")
        assert "Protected files" in self.selenium.page_source
