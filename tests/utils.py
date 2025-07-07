import os

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.core.utils import read_version_from_cmd 
from webdriver_manager.core.os_manager import PATTERN
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from playwright.sync_api import sync_playwright


class PlaywrightChromeTestCase(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
        super().setUpClass()
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.browser.close()
        cls.playwright.stop()


class SeleniumChromeTestCase(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        version = read_version_from_cmd('/usr/bin/google-chrome --version', PATTERN['google-chrome'])
        options = webdriver.ChromeOptions()
        options.add_argument('-headless')
        options.add_argument('-no-sandbox')
        cls.selenium = webdriver.Chrome(service=ChromeService(ChromeDriverManager(driver_version=version).install()), options=options)
        cls.selenium.implicitly_wait(1)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()


class SeleniumFirefoxTestCase(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        version = read_version_from_cmd("/usr/bin/firefox --version", PATTERN["firefox"])
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        options.add_argument('-no-sandbox')
        cls.selenium = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        cls.selenium.implicitly_wait(1)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()