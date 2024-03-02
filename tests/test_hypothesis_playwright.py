import json
import os
import subprocess
import urllib

import pytest
from dotenv import load_dotenv
from playwright.sync_api import expect, sync_playwright
from hypothesis import given, strategies as st

load_dotenv()

capabilities = {
    'browserName': 'Chrome',  # Browsers allowed: `Chrome`, `MicrosoftEdge`, `pw-chromium`, `pw-firefox` and `pw-webkit`
    'browserVersion': 'latest',
    'LT:Options': {
        'platform': 'Windows 11',
        'build': 'Playwright Locators Demo Build',
        'name': 'Playwright Locators Test For Windows 11 & Chrome',
        'user': os.getenv('LT_USERNAME'),
        'accessKey': os.getenv('LT_ACCESS_KEY'),
        'network': True,
        'video': True,
        'visual': True,
        'console': True,
        'tunnel': False,   # Add tunnel configuration if testing locally hosted webpage
        'tunnelName': '',  # Optional
        'geoLocation': '', # country code can be fetched from https://www.lambdatest.com/capabilities-generator/
    }
}


# @pytest.fixture(name="local_grid_page")
# def playwright_local_grid_page():
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=True)
#         page = browser.new_page()
#         yield page

# @pytest.fixture(name="cloud_grid_page")
# def playwright_local_grid_page():    
#     with sync_playwright() as playwright:
#         playwrightVersion = str(subprocess.getoutput('playwright --version')).strip().split(" ")[1]
#         capabilities['LT:Options']['playwrightClientVersion'] = playwrightVersion        
#         lt_cdp_url = 'wss://cdp.lambdatest.com/playwright?capabilities=' + urllib.parse.quote(json.dumps(capabilities))    
#         browser = playwright.chromium.connect(lt_cdp_url)
#         page = browser.new_page()    
#         yield page


# replace cloud_grid_page with local_grid_page while running on local
def interact_with_lambdatest(quantity):
     with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()         
        page.goto("https://ecommerce-playground.lambdatest.io/")
        page.get_by_role("button", name="Shop by Category").click()
        page.get_by_role("link", name="MP3 Players").click()
        page.get_by_role("link", name="HTC Touch HD HTC Touch HD HTC Touch HD HTC Touch HD").click()        
        page.get_by_role("button", name="Add to Cart").click(click_count=quantity)
        page.get_by_role("link", name="Checkout ").first.click()
        unit_price = float(page.get_by_role("cell", name="$146.00").inner_text().replace("$",""))
        total_price = quantity * unit_price
        page.screenshot("final.png")
        return total_price
        


# Hypothesis strategy for generating product names and quantities
quantity_strategy = st.integers(min_value=1, max_value=10)

# Use Hypothesis to generate test cases for interacting with the website
@given(quantity=quantity_strategy)
def test_website_interaction(quantity):    
    assert interact_with_lambdatest(quantity) == quantity * 146.00
    
