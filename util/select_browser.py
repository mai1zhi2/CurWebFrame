from util.read_ini import ReadIni
from selenium import webdriver
def select_brower():
    read_ini = ReadIni(node='webdriver')
    web_driver = read_ini.get_key('webdriver')
    for wd in web_driver:
        if wd == 'firefox':
            return webdriver.Firefox()
        elif wd == 'ie':
            return webdriver.Ie()
        elif wd == '360':
            wd_option = read_ini.get_value('360')
            chrome_options = webdriver.ChromeOptions()
            chrome_options.binary_location = wd_option
            chrome_options.add_argument(r'--lang=zh-CN')
            return webdriver.Chrome(chrome_options=chrome_options)
        elif wd == 'chrome':
            return webdriver.Chrome()

