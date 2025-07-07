import re

from django.contrib.auth import get_user_model
from django.conf import settings

from playwright.sync_api import expect

from protected657.tests.utils import PlaywrightChromeTestCase
from protected657.models import ProtectedFile

User = get_user_model()


class ProtectedFilesAdminUserTest(PlaywrightChromeTestCase):

    USERNAME = "playtester"
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
        self.page = self.browser.new_page()
        self.page.goto(f"{self.live_server_url}/admin/login/")
        self.page.wait_for_selector('text=Django administration')
        self.page.fill('[name=username]', self.USERNAME)
        self.page.fill('[name=password]', self.PASSWORD)
        self.page.click('text=Log in')
        expect(self.page).to_have_title(re.compile("Site administration | Django site admin"))

    def testProtectedFiles(self):
        self.page.goto(f"{self.live_server_url}/protected/")
        expect(self.page.get_by_text('Protected files')).to_be_visible()

    def testAddAndDeleteProtectedFiles(self):
        # Test to upload
        self.page.goto(f"{self.live_server_url}/protected/")
        self.page.get_by_role('link', name='Add File').click()
        self.page.get_by_role('textbox', name='Title:').click()
        self.page.get_by_role('textbox', name='Title:').fill('Playwright test')
        self.page.get_by_role('button', name='File:').set_input_files(self.UPLOADFILE)
        self.page.get_by_role('button', name='Submit').click()
        protected_files = ProtectedFile.objects.filter(created_by=self.user1)
        assert protected_files.count() == 1
        protected_file_name = protected_files[0].file.name
        # Test to download
        self.page.goto(f"{self.live_server_url}/protected/")
        with self.page.expect_download() as download_info:
            # Perform the action that initiates download
            self.page.get_by_role('link', name=protected_file_name).click()
        download = download_info.value
        assert download.suggested_filename == protected_file_name
        # Test to delete
        self.page.goto(f"{self.live_server_url}/admin/")
        self.page.get_by_role('link', name='Protected files' ).click()
        self.page.get_by_role('link', name='Playwright test').click()
        self.page.get_by_role('link', name='Delete', exact=True ).click()
        self.page.get_by_role('button', name='Yes, I’m sure' ).click()
        protected_files = ProtectedFile.objects.filter(created_by=self.user1)
        assert protected_files.count() == 0
        # Log out
        self.page.get_by_role('button', name='Log out' ).click()

    def testLoginAnonUser(self):
        page = self.browser.new_page()
        page.goto(f"{self.live_server_url}/admin/")
        page.wait_for_selector('text=Django administration')
        page.fill('[name=username]', 'anonuser')
        page.fill('[name=password]', 'secret')
        page.click('text=Log in')
        assert len(page.eval_on_selector(".errornote", "el => el.innerText")) > 0
        page.close()