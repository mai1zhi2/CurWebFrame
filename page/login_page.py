from base.find_element import FindElement
class LoginPage:
    def __init__(self,driver,node):
        self.driver = driver
        self.fd = FindElement(self.driver,node)

    #获取账户
    def get_username_element(self):
        return self.fd.get_element('user_name')

    #获取密码
    def get_password_element(self):
        return self.fd.get_element('password')

    #获取登录按钮
    def get_button_element(self):
        return self.fd.get_element('login_button')

    #获取错误信息
    def get_error_element(self):
        return self.fd.get_element('error')

    #获取正确登录信息
    def get_success_element(self):
        return self.fd.get_element('confirm_login')