from django.contrib.auth import get_user_model
from django.conf import settings

from selenium.webdriver.common.by import By

from protected657.tests.utils import SeleniumChromeTestCase, SeleniumFirefoxTestCase
from protected657.models import ProtectedFile

User = get_user_model()


class ProtectedFilesAdminUserTest(SeleniumChromeTestCase):

    USERNAME = "testare1"
    PASSWORD = "password1234"
    UPLOADFILE = f"{settings.BASE_DIR}/protected657/door_logo43.png"

    def setUp(self):
        # Create a user to login with
        self.user1 = User.objects.create_user(
            username=self.USERNAME,
            email="test1@example.com",
            password=self.PASSWORD,
            is_staff=True,
            is_superuser=True,
        )
        self.selenium.get(f"{self.live_server_url}/admin/login/")
        self.selenium.implicitly_wait(0.5)
        login_form = self.selenium.find_element(By.ID, "login-form")
        username = login_form.find_element(By.NAME, "username")
        username.send_keys(self.USERNAME)
        username = login_form.find_element(By.NAME, "password")
        username.send_keys(self.PASSWORD)
        submit_row = login_form.find_element(By.CLASS_NAME, "submit-row")
        submit_button = submit_row.find_element(By.CSS_SELECTOR, "input")
        submit_button.click()
        self.selenium.implicitly_wait(0.5)
        assert self.selenium.title == "Site administration | Django site admin"
    
    def testProtectedFiles(self):
        self.selenium.get(f"{self.live_server_url}/protected/")
        self.selenium.implicitly_wait(0.5)
        assert "Protected files" in self.selenium.page_source

    def testAddAndDeleteProtectedFiles(self):
        self.selenium.get(f"{self.live_server_url}/protected/add/")
        self.selenium.implicitly_wait(0.5)
        assert "Add File" in self.selenium.page_source
        title_input = self.selenium.find_element(By.ID, "id_title")
        title_input.send_keys("Selenium test")
        self.selenium.find_element(By.ID,"id_file").send_keys(self.UPLOADFILE)
        self.selenium.find_element(By.TAG_NAME, "button").click()
        self.selenium.implicitly_wait(0.5)
        assert self.selenium.page_source.find("Selenium test")
        assert "Protected files" in self.selenium.page_source
        protected_files = ProtectedFile.objects.filter(created_by=self.user1)
        assert protected_files.count() == 1
        # Test delete the file.
        self.selenium.get(f"{self.live_server_url}/admin/")
        self.selenium.implicitly_wait(0.5)
        assert "Protected files" in self.selenium.page_source
        self.selenium.find_element(By.LINK_TEXT, "Protected files").click()
        self.selenium.implicitly_wait(0.5)
        self.selenium.find_element(By.LINK_TEXT, "Selenium test").click()
        self.selenium.implicitly_wait(0.5)
        assert self.selenium.page_source.find("Selenium test")
        self.selenium.find_elements(By.CLASS_NAME, "deletelink")[0].click()
        self.selenium.implicitly_wait(0.5)
        self.selenium.find_element(By.XPATH, "//input[@type='submit']").click()
        assert self.selenium.page_source.find("Selenium test")
        assert 'The protected file “Selenium test” was deleted successfully.' in self.selenium.page_source
        protected_files = ProtectedFile.objects.filter(created_by=self.user1)
        assert protected_files.count() == 0


class ProtectedFilesUserTest(SeleniumFirefoxTestCase):

    USERNAME = "testare2"
    PASSWORD = "password1234"
    UPLOADFILE = f"{settings.BASE_DIR}/protected657/door_logo43.png"

    def setUp(self):
        # Create a user to login with
        self.user2 = User.objects.create_user(
            username=self.USERNAME,
            email="test2@example.com",
            password=self.PASSWORD,
            is_staff=True,
        )
        self.selenium.get(f"{self.live_server_url}/admin/login/")
        self.selenium.implicitly_wait(0.5)
        login_form = self.selenium.find_element(By.ID, "login-form")
        username = login_form.find_element(By.NAME, "username")
        username.send_keys(self.USERNAME)
        username = login_form.find_element(By.NAME, "password")
        username.send_keys(self.PASSWORD)
        submit_row = login_form.find_element(By.CLASS_NAME, "submit-row")
        submit_button = submit_row.find_element(By.CSS_SELECTOR, "input")
        submit_button.click()
        self.selenium.implicitly_wait(0.5)
        assert self.selenium.title == "Site administration | Django site admin"
    
    def testAdmin(self):
        self.selenium.get(f"{self.live_server_url}/admin/")
        self.selenium.implicitly_wait(0.5)
        assert "You don’t have permission to view or edit anything." in self.selenium.page_source

    def testProtectedFiles(self):
        self.selenium.get(f"{self.live_server_url}/protected/")
        self.selenium.implicitly_wait(0.5)
        assert "Protected files" in self.selenium.page_source

    def testAddProtectedFiles(self):
        self.selenium.get(f"{self.live_server_url}/protected/add/")
        self.selenium.implicitly_wait(0.5)
        assert "Add File" in self.selenium.page_source
        title_input = self.selenium.find_element(By.ID, "id_title")
        title_input.send_keys("Selenium test")
        self.selenium.find_element(By.ID,"id_file").send_keys(self.UPLOADFILE)
        self.selenium.find_element(By.TAG_NAME, "button").click()
        self.selenium.implicitly_wait(0.5)
        assert self.selenium.page_source.find("Selenium test")
        assert "Protected files" in self.selenium.page_source
        protected_files = ProtectedFile.objects.filter(created_by=self.user2)
        for pf in protected_files:
            pf.delete()
        protected_files = ProtectedFile.objects.filter(created_by=self.user2)
        assert protected_files.count() == 0