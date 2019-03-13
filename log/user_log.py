import logging
import os
import time
import datetime
from util import read_ini

log_level = read_ini.ReadIni(node='loglevel').get_value('level')

class UserLog:

    level = 'default'
    def __init__(self):
        self.logger = logging.getLogger('')
        self.logger.handlers = []
        self.logger.removeHandler(self.logger.handlers)
        self.logger.setLevel(logging.DEBUG)
        if not self.logger.handlers:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            log_dir = os.path.join(base_dir, "logs")
            log_file = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
            log_name = log_dir + '\\' + log_file
            if not os.path.isdir(log_dir):
                os.makedirs(log_dir)
            if not os.path.isfile(log_name):
                fd = open(log_name, mode='w', encoding='utf-8')
                fd.close()
            self.file_handle = logging.FileHandler(log_name, 'a', encoding='utf-8')
            formatter = logging.Formatter(
                '%(asctime)s ----- %(filename)s----- %(funcName)s ----- %(levelno)s: %(levelname)s -----%(message)s')
            self.file_handle.setFormatter(formatter)
            self.logger.addHandler(self.file_handle)

    def get_log(self):
        return self.logger

    def close_handle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()

if __name__ == '__main__':
    user = UserLog()
    log = user.get_log()
    log.debug('test')
    user.close_handle()