from playwright.sync_api import Page
from utils.commonClick import commonClick


class LoginPage:
    
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.LOGIN_URL = f"{base_url}/"
        self.click = commonClick(page)
   
    def goto_login_page(self):
        self.page.goto(self.LOGIN_URL)
        #self.click.click_by_xpath('//*[contains(@class, "c-gnb__item-link") and contains(@class, "c-gnb__item-link--utility-top") and contains(@class, "icon-my")]')
        # locator = self.page.locator('//*[contains(@class, "c-gnb__item-link") and contains(@class, "c-gnb__item-link--utility-top") and contains(@class, "icon-my")]')
        # if locator.count() > 0:
        #     locator.wait_for(state='visible', timeout=30000)  # Wait for the element to be visible
        #     locator.click()
        # else:
        #     #self.click.click_by_xpath('//*[contains(@class, "c-gnb__item-link") and contains(@class, "c-gnb__item-link--utility-top") and contains(@class, "icon-my")]')
        #     print("Element not found or not visible")
        #     raise Exception("Element not found or not visible") 
    
    def login(self):
        self.page.wait_for_selector("#email", state="visible", timeout=60000) # Wait for the email input to be visible
        self.page.fill("#email", "lgc.jinwon+ukpc1@gmail.com")
        self.page.wait_for_selector("#password", state="visible", timeout=60000) # Wait for the email input to be visible
        self.page.fill("#password", "Lg@156699")
        self.click.click_by_id('button_user-login')
        
        print("Test completed")