from handle.forgetpass_handle import ForgetpassHandle

class ForgetpassBusiness:
    def __init__(self,driver,node):
        self.driver = driver
        self.forgetpass_h = ForgetpassHandle(self.driver,node)

    def user_base(self,username):
        self.forgetpass_h.send_username(username)
        self.forgetpass_h.click_forget_button()

    def forgetpass_function(self,username,assertCode,assertText):
        self.user_base(username)
        if assertText in self.forgetpass_h.get_text(assertCode):
            return True
        else:
            return False
