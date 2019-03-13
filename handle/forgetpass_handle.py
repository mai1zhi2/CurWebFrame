from page.forgetpass_page import ForgetpassPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from log.user_log import UserLog

class ForgetpassHandle:
    def __init__(self,driver,node):
        self.driver = driver
        get_user_log = UserLog()
        self.user_log = get_user_log.get_log()
        self.forgetpass_p = ForgetpassPage(self.driver,node)

    def send_username(self,username):
        self.forgetpass_p.get_username_element().clear()
        self.user_log.info("输入的用户名是：" + username)
        self.forgetpass_p.get_username_element().send_keys(username)

    def click_forget_button(self):
        self.user_log.info("点击忘记密码按钮" )
        self.forgetpass_p.get_button_element().click()

    def get_text(self,assertCode):
        try:
            if assertCode == "send_success":
                #time.sleep(10)
                locator = (By.CLASS_NAME,'message')
                WebDriverWait(self.driver,10,0.5).until(EC.visibility_of_element_located(locator))
                text = self.forgetpass_p.get_success_element().text
            else:
                text = self.forgetpass_p.get_error_element().text
        except:
            text = None
        return text