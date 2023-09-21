'''
Created on 2022-09-08

@author: wf
'''
import asyncio

from selenium.webdriver.remote.webdriver import BaseWebDriver
from selenium.webdriver.support.wait import WebDriverWait

from tests.base_server_test import BaseAsynctest
from tests.browser_test import SeleniumBrowsers
from tests.basetest import Basetest
from examples.basedemo import Demo

class BaseSeleniumTest(BaseAsynctest):
    """
    Base class for Selenium tests
    """
    
    async def asyncSetUp(
        self, 
        # default testport
        port:int=8193, 
        host:str="127.0.0.1", 
        sleep_time=None, 
        with_server=True, 
        debug=False, 
        profile=True, 
        mode=None):
        await BaseAsynctest.asyncSetUp(self, port=port, host=host, sleep_time=sleep_time, with_server=with_server, debug=debug, profile=profile, mode=mode)
        await asyncio.sleep(self.server.sleep_time)
        self.browser = SeleniumBrowsers(headless=Basetest.inPublicCI()).getFirst()
        
    async def getBrowserForDemo(self):
        """
        get the browser for a Demo test
        """
        browser=SeleniumBrowsers(headless=Basetest.inPublicCI()).getFirst()
        await asyncio.sleep(self.server.sleep_time)
        Demo.testmode = True
        return browser

    def get_waiting_browser(self, browser: BaseWebDriver, timeout: float = 5.0):
        """
        Return a waiting webdriver for the given driver/browser

        Args:
            browser: WebDriver
            timeout: maximum time to wait
        """
        driver = WebDriverWait(browser, timeout)
        return driver
