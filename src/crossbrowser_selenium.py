from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import urllib3
import warnings
import os
from os import environ
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.remote.remote_connection import RemoteConnection
from hypothesis.strategies import integers
from dotenv import load_dotenv

load_dotenv()

# Get username and access key of the LambdaTest Platform
username = os.getenv('LT_USERNAME', None)
access_key = os.getenv('LT_ACCESS_KEY', None)

class CrossBrowserSetup(object):
    global web_driver

    def __init__(self):
        global remote_url

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        remote_url = "https://" + str(username) + ":" + str(access_key) + "@hub.lambdatest.com/wd/hub"

    def add(self, browsertype):
        if (browsertype == "Firefox"):
            ff_options = webdriver.FirefoxOptions()
            ff_options.browser_version = "latest"
            ff_options.platform_name = "Windows 11"

            lt_options = {}
            lt_options["build"] = "Build: FF: Hypothesis Testing with Selenium & Pytest"
            lt_options["project"] = "Project: FF: Hypothesis Testing withSelenium & Pytest"
            lt_options["name"] = "Test: FF: Hypothesis Testing with Selenium & Pytest"

            lt_options["browserName"] = "Firefox"
            lt_options["browserVersion"] = "latest"
            lt_options["platformName"] = "Windows 11"

            lt_options["console"] = "error"
            lt_options["w3c"] = True
            lt_options["headless"] = False

            ff_options.set_capability('LT:Options', lt_options)

            web_driver = webdriver.Remote(
                command_executor = remote_url,
                options = ff_options
            )
            self.driver = web_driver
            self.driver.get("https://www.lambdatest.com")            
            sleep(1)
            if web_driver is not None:
                web_driver.execute_script("lambda-status=passed")
                web_driver.quit()
                return True
            else:
                web_driver.execute_script("lambda-status=failed")
                web_driver.quit()
                return False

