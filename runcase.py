import unittest
import os
import datetime
from util import mkdir
from util.HTMLTestRunner_cn import HTMLTestRunner
from util.send_email import Sendmail

# case_path = os.path.join(os.getcwd(),'case')
# print (case_path)
starttime = datetime.datetime.now()
file_path = mkdir.makedir() + '.html'
suite = unittest.defaultTestLoader.discover(os.getcwd(),'*_case.py')
runer = HTMLTestRunner(title="测试报告", description="wordpress测试报告", stream=open(file_path, "wb+"),
                           verbosity=2, retry=2, save_last_try=True)
runer.run(suite)
endtime = datetime.datetime.now()
runningtime = (endtime-starttime).seconds
Sendmail(runningtime).send_mail()
