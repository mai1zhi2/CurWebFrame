from page.login_page import LoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from log.user_log import UserLog
from util.read_ini import ReadIni
import json

class LoginHandle:
    def __init__(self,driver,node):
        self.driver = driver
        get_user_log = UserLog()
        self.user_log = get_user_log.get_log()
        self.login_p = LoginPage(self.driver,node)

    #输入用户
    def send_username(self,username):
        self.login_p.get_username_element().clear()
        self.user_log.info("输入的用户名是：" + username)
        self.login_p.get_username_element().send_keys(username)

    #输入密码
    def send_password(self,password):
        self.user_log.info("输入的密码是：" + password)
        self.login_p.get_password_element().send_keys(password)

    #点击登录
    def click_login_button(self):
        self.user_log.info("点击登录按钮" )
        self.login_p.get_button_element().click()

    # 获取错误信息
    def get_text(self,assertCode):
        try:
            if assertCode == "login_success":
                #time.sleep(10)
                locator = (By.ID,'footer-thankyou')
                WebDriverWait(self.driver,10,0.5).until(EC.visibility_of_element_located(locator))
                text = self.login_p.get_success_element().text
                cookies = self.driver.get_cookies()
                with open(ReadIni(node='cookies').get_value('cookies'),'w') as c:
                    json.dump(cookies,c)
            else:
                text = self.login_p.get_error_element().text
        except:
            text = None
        return text


