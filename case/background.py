from selenium import webdriver
import json
import time
def read_cookies():
    driver = webdriver.Firefox()
    driver.get("http://captain.live/")
    time.sleep(1)
    with open("C:/Users/Administrator/PycharmProjects/CurWebFrame/config/cookies.json", "r") as fp:
        cookies = json.load(fp)
        for cookie in cookies:
            print(cookie)
            cookie.pop('domain')  # 如果报domain无效的错误
            driver.add_cookie(cookie_dict=cookie)
    driver.get("http://captain.live/wp-admin/")
    driver.close()
read_cookies()