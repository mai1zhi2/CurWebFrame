import configparser
class ReadIni:
    def __init__(self,file_name=None,node=None):
        if file_name == None:
            file_name = "C:\\Users\\Administrator\\PycharmProjects\\CurWebFrame\\config\\LocalElement.ini"
        if node == None:
            self.node = "Login_ddt_case_element"
        else:
            self.node = node
        self.cf = self.load_ini(file_name)

    #加载文件
    def load_ini(self,file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf

    #获取value的值
    def get_value(self,key):
        data = self.cf.get(self.node,key)
        return data

    def get_key(self,key):
        return self.cf.options(key)

# if __name__ == '__main__':
#    read_init = ReadIni()
#    print(read_init.get_value('user_name'))