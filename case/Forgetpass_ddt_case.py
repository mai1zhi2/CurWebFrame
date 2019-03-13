import ddt
import unittest
import os
from selenium import webdriver
from util.HTMLTestRunner_cn import HTMLTestRunner
import time
from util import mkdir
from util.read_ini import ReadIni
from business import forgetpass_business
from util import select_browser

@ddt.ddt
class ForgetpassDdtCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = select_browser.select_brower()



    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True


    def setUp(self):
        node = os.path.splitext(os.path.basename(__file__))[0] + '_element'
        self.driver.implicitly_wait(10)
        #time.sleep(2)
        self.driver.get('http://captain.live/wp-login.php?action=lostpassword')
        self.forgetpass = forgetpass_business.ForgetpassBusiness(self.driver, node)

    def tearDown(self):
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @ddt.data(
        ['xxx','username_error','无效的用户名或电子邮件地址'],
        ['xxx@qq.com', 'send_success', '请在您的电子邮箱中检查确认链接'],
        ['', 'no_username', '请输入用户名或电子邮件地址']
    )
    @ddt.unpack
    def test_forgetpass_case(self,username,assertCode,assertText):
        '''
            忘记密码
        '''
        Result = self.forgetpass.forgetpass_function(username,assertCode,assertText)
        self.assertTrue(Result, "测试失败")
        self.add_img()

