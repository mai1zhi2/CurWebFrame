import yaml
class ReadYaml:
    def __init__(self,file_name=None):
        if file_name == None:
            file_name = "C:\\Users\\Administrator\\PycharmProjects\\CurWebFrame\\config\\data.yaml"
        with open(file_name, 'r', encoding='utf-8') as f:
            self.data = yaml.load(f)

    def get_value(self,key):
        return self.data[key]

if __name__ =='__main__':
    r = ReadYaml()
    print (r.get_value('Login_ddt_case'))