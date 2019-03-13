from util.read_ini import ReadIni
from log.user_log import UserLog
import os
class FindElement:
    def __init__(self,driver,node):
        self.driver = driver
        get_user_log = UserLog()
        self.user_log = get_user_log.get_log()
        self.node = node
        print(self.node)

    def get_element(self,key):
        read_ini = ReadIni(node=self.node)
        data = read_ini.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        self.user_log.info("定位方式:"+by+"-----定位值:"+value)

        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'classname':
                return self.driver.find_element_by_class_name(value)
            elif by == 'tag':
                return self.driver.find_element_by_tag_name(value)
            elif by == 'css':
                return self.driver.find_element_by_css_selector(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            return None