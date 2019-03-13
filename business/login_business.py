from handle.login_handle import LoginHandle

class LoginBusiness:
    def __init__(self,driver,node):
        self.driver = driver
        self.login_h = LoginHandle(self.driver,node)

    def user_base(self,username,password):
        self.login_h.send_password(password)
        self.login_h.send_username(username)
        self.login_h.click_login_button()


    def login_function(self,username,password,assertCode,assertText):
        self.user_base(username,password)
        if assertText in self.login_h.get_text(assertCode):
            return True
        else:
            return False