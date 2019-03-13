import time
import ddt
import unittest
import os
from selenium import webdriver
from business import login_business
from util.HTMLTestRunner_cn import HTMLTestRunner
import time
from util import mkdir
from util.read_ini import ReadIni
#from util.excel_util import ExcelUtil
from util.read_yaml import ReadYaml
from log.user_log import UserLog
from util import select_browser
log = UserLog()
logger = log.get_log()
yaml_data = ReadYaml().get_value(os.path.splitext(os.path.basename(__file__))[0])


@ddt.ddt
class LoginDdtCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = select_browser.select_brower()

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def setUp(self):
        self.driver.implicitly_wait(10)
        #time.sleep(2)
        self.driver.get('http://captain.live/wp-login.php')
        node = os.path.splitext(os.path.basename(__file__))[0] + '_element'
        self.login = login_business.LoginBusiness(self.driver,node)

    def tearDown(self):
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @ddt.data(
        ["xxx@qq.com","password","login_success","感谢使用"],
        ["xxx@qq.com","pass","password_error","密码无效"],
        ["q.com","7kNQ@1v*lItFYa$)","username_error","无效用户名"],
        ["xxx@qq.com", "", "no_password", "为空"]
    )
    @ddt.unpack
    def test_login_case(self,username,password,assertCode,assertText):
        '''
            用户登录
        '''
        Result = self.login.login_function(username,password,assertCode,assertText)
        self.assertTrue(Result,"测试失败")
        self.add_img()

if  __name__  == "__main__":
    file_path = mkdir.makedir() + '.html'
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginDdtCase)
    runer = HTMLTestRunner(title="测试报告", description="wordpress测试报告", stream=open(file_path, "wb+"),
                           verbosity=2, retry=2, save_last_try=True)
    runer.run(suite)

