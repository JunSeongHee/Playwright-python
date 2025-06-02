from playwright.sync_api import Page
from utils.commonClick import commonClick


class LoginPage:
    
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.LOGIN_URL = f"{base_url}/"
        self.click = commonClick(page)
   
    def goto_login_page(self):
        self.page.goto(self.LOGIN_URL)
        self.click.click_by_xpath('//*[contains(@class, "c-gnb__item-link") and contains(@class, "c-gnb__item-link--utility-top") and contains(@class, "icon-my")]')   
    
    def login(self):
        self.page.fill("#email", "lgc.jinwon+ukpc1@gmail.com")   
        self.page.fill("#password", "Lg@156699")
        self.click.click_by_id('button_user-login')
        
        print("Test completed")